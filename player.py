import pyxel


class Player:
    def __init__(self, x, y):
        # Player variables
        self.x = x
        self.y = y

        self.dx = 1.0
        self.dy = 0
        self.speed = 0.8

        self.playerWidth = 8

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

        '''
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        '''

    def Draw(self):
        u = (pyxel.frame_count // 8 % 3 + 1) * 8 if self.leftDown or self.rightDown else 8
        v = 8 if self.direction == 1 else -8
        pyxel.blt(self.x, self.y, 1, u, 0, v, 16, 0)

    def Move(self):
        if self.leftDown:
            self.direction = -1
            if self.dx > 0.0:
                self.dx = self.speed
                self.dx = -self.dx
            if self.x > 0:
                self.x += self.dx

        if self.rightDown:
            self.direction = 1
            if self.dx < 0.0:
                self.dx = self.speed
            if self.x + self.playerWidth < 128:
                self.x += self.dx

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
