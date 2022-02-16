import pyxel

class Player() :
    def __init__(self, x, y) :
        # Player variables
        self.x = x
        self.y = x

        pyxel.load("greenknight.pyxres", True, True, False, False)


        
        '''
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )
        '''
        
    # Draws the player 
    def Draw(self):
        pyxel.blt(self.x, self.y, 1, 8, 0, 8, 16, 0 )

    def Update(self):
        # Player controls
        if pyxel.btn(pyxel.KEY_LEFT) :
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.x +=1
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP) :
            self.y -=1
