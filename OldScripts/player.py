import pyxel as pyx

COLLIDE_X = 4
TILE_FLOOR = (5, 0)


def getTile(x, y):
    """ Gets a tile from the displayed tile-map and returns the tile's x and y from the image bank """
    return pyx.tilemap(0).pget(x, y)


def detectTile(x, y, dy):
    """ Checks if player x collides with any tiles that player can collide off of """
    x1 = int(x // 8)
    y1 = int(y // 8)
    x2 = int((x + 8) // 8)
    y2 = int((y + 8) // 8)
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if getTile(xi, yi)[0] >= COLLIDE_X:
                return True

    if dy > 0 and y % 8 == 1:
        for xi in range(x1, x2 + 1):
            if getTile(xi, y1 + 1) == TILE_FLOOR:
                return True
    return False


class Player:
    """ Creates a player object that accepts input, collides and is animated """

    def __init__(self, x, y):
        # Player variables
        self.x = x
        self.y = y

        self.dx = 1
        self.dy = 0
        self.speed = 0.8
        self.jumpHeight = 5

        # Keyboard Variables
        self.leftDown = False
        self.rightDown = False
        self.haveJumped = False
        self.direction = 1

        # Buttons
        self.right = pyx.KEY_D
        self.left = pyx.KEY_A
        self.jump = pyx.KEY_SPACE

        pyx.load("../Assets/greenknight.pyxres")

    def Draw(self):
        """ Animates the player """

        # u is the variable that holds the actual image from the image bank.
        # It loops through the images using calculations
        u = (pyx.frame_count // 6 % 3 + 1) * 8 if self.leftDown or self.rightDown else 8

        # v decides if the image needs to be flipped. Positive for no, negative for yes.
        v = 8 if self.direction == 1 else -8
        pyx.blt(self.x, self.y, 1, u, 0, v, 16, 0)

    def Move(self):
        """ Alters player x and y based on direction x and y and player input """

        # Checks if leftDown is true, then move the player
        if self.leftDown:
            self.direction = -1
            if not detectTile(self.x, self.y, self.dy):
                self.x -= self.dx

        # Checks if rightDown is true, then move the player
        if self.rightDown:
            self.direction = 1
            if not detectTile(self.x + 1, self.y, self.dy):
                self.x += self.dx

    def UpdateControls(self):
        """ Checks if the player pressed any keys and call Move function """
        pyx.tilemap(0).pset(3, 0, TILE_FLOOR)

        # Checking button presses
        if pyx.btnp(self.left):
            self.leftDown = True

        if pyx.btnp(self.right):
            self.rightDown = True

        # Checking button releases
        if pyx.btnr(self.left):
            self.leftDown = False
            self.dx = self.speed

        if pyx.btnr(self.right):
            self.rightDown = False
            self.dx = self.speed

        if pyx.btnr(self.jump):
            if not self.haveJumped:
                self.haveJumped = True
                self.dy = self.jumpHeight

        self.Move()
