import pyxel

COLLIDE_X = 4


def getTile(x, y):
    return pyxel.tilemap(0).pget(x, y)


def detectTile(x, y, dy):
    x1 = int(x // 8)
    y1 = int(y // 8)
    x2 = int((x + 8) // 8)
    y2 = int((y + 8) // 8)
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if getTile(xi, yi)[0] >= COLLIDE_X:
                return True
            # pyxel.tilemap(0).pset(xi, yi, (0, 0))

    return False


class Player:
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

        pyxel.load("greenknight.pyxres")

    def Draw(self):
        u = (pyxel.frame_count // 6 % 3 + 1) * 8 if self.leftDown or self.rightDown else 8
        v = 8 if self.direction == 1 else -8
        pyxel.blt(self.x, self.y, 1, u, 0, v, 16, 0)

    def Move(self):
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
