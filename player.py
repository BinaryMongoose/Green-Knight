import pyxel

class Player() :
    def __init__(self, x, y) :
        # Player variables
        self.x = x
        self.y = x

        self.dx = 0
        self.dy = 0

        self.direction = 1

        pyxel.load("greenknight.pyxres", True, True, False, False)

        '''
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        '''
        
    # Draws the player 
    def Draw(self):
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )

    def Move(self):
        self.x += self.dx
        self.y += self.dy
            
    def UpdateControls(self):
        if pyxel.btn(pyxel.KEY_LEFT) :
            self.dx = -1
            self.Move()
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.dx = 1
            self.Move()
        if pyxel.btn(pyxel.KEY_UP) :
            self.dy = -1
            self.Move()
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.dy = 1
            self.Move()
        else :
            self.dx = 0
            self.dy = 0
        
    def Animate(self) :
        pass
