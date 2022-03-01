import pyxel

COLLIDE_X = 4


def getTile(x, y):
    """ Gets a tile from the displayed tile-map and returns the tile's x and y from the image bank """
    return pyxel.tilemap(0).pget(x, y)


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

    return False


class Player:
    """ Creates a player object that accepts input, collides and is animated """
    def __init__(self, x, y):
        # Player variables
        self.x = x
        self.y = y

        self.dx = 1.0
        self.dy = 0
        self.speed = 0.8

        # Keyboard Variables
        self.leftDown = False
        self.rightDown = False
        self.haveJumped = False
        self.direction = 1

        # Buttons
        self.right = pyxel.KEY_D
        self.left = pyxel.KEY_A
        self.jump = pyxel.KEY_SPACE

        pyxel.load("../Assets/greenknight.pyxres")

    def Draw(self):
        """ Animates the player """
        u = (pyxel.frame_count // 6 % 3 + 1) * 8 if self.leftDown or self.rightDown else 8
        v = 8 if self.direction == 1 else -8
        pyxel.blt(self.x, self.y, 1, u, 0, v, 16, 0)

    def Move(self):
        """ Alters player x and y based on direction x and y and player input """
        if self.leftDown:
            self.direction = -1
            if not detectTile(self.x, self.y, self.dy):
                self.x -= self.dx
            else:
                pass

        if self.rightDown:
            self.direction = 1
            if not detectTile(self.x + 1, self.y, self.dy):
                self.x += self.dx
            else:
                pass

    def UpdateControls(self):
        """ Checks if the player pressed any keys and call Move function """
        if pyxel.btnp(self.left):
            self.leftDown = True
        if pyxel.btnp(self.right):
            self.rightDown = True

        if pyxel.btnr(self.left):
            self.leftDown = False
            self.dx = self.speed
        if pyxel.btnr(self.right):
            self.rightDown = False
            self.dx = self.speed

        self.Move()
