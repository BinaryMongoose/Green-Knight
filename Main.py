import pyxel

player = None

class App():
    def __init__(self):
        # Initiate Window
        pyxel.init(128, 88, "Ya Ya's Game")

        pyxel.load("greenknight.pyxres", True, True, False, False)

        global player
        player = Player(0, 0)
        
        # Run Application
        pyxel.run(self.Update, self.Draw)

    def Update(self):
        # Calls everythin in update player every frame
        player.Update()

    def DrawMap(self) :
        # Drawing the tileset
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 1200, 94)

        # Drawing text
        pyxel.text(2, 66, "Player Y: " + str(player.y), 7)
        pyxel.text(2, 73, "Player X: " + str(player.x), 7)

    # Draws all objects listed every frame
    def Draw(self) :
        self.DrawMap()
        
        # Draws player every frame.
        player.Draw()
        
class Player() :
    def __init__(self, x, y) :
        # Player variables
        self.x = x
        self.y = x
        
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
            self.x = 1
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.x +=1
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.y += 1
        if pyxel.btn(pyxel.KEY_UP) :
            self.y -=1


App()
