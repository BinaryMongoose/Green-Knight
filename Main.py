import pyxel
print("Hello World!")
class App():
    def __init__(self):
        # Initiate Window
        pyxel.init(128, 88, "Ya Ya's Game")

        pyxel.load("CastleSet.pyxres", True, True, False, False)
        
        # Player variables
        self.playerx = 0
        self.playery = 35
        self.playerColor = 2

        # Run Application
        pyxel.run(self.Update, self.Draw)

    def Update(self):
        # Calls everythin in update player every frame
        self.UpdatePlayer()

    def UpdatePlayer(self):

        # Player controls
        if pyxel.btn(pyxel.KEY_LEFT) :
            self.playerx -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) :
            self.playerx +=1
        if pyxel.btn(pyxel.KEY_DOWN) :
            self.playery += 1
        if pyxel.btn(pyxel.KEY_UP) :
            self.playery -=1

        if pyxel.btn(pyxel.KEY_W) :
            self.playerColor += 1
            if self.playerColor == 16 :
                self.playerColor = 1

    def DrawMap(self) :
        # Drawing the tileset
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 1200, 94)

        # Drawing text
        #pyxel.text(2, 66, "Player Y: " + str(self.playery), 7)
        #pyxel.text(2, 73, "Player X: " + str(self.playerx), 7)
        
    # Draws the player 
    def DrawPlayer(self):
        pyxel.blt(self.playerx, self.playery, 0, 0, 16, 8, 16, 0 )


    # Draws all objects listed every frame
    def Draw(self) :
        self.DrawMap()
        # Draws player every frame.
        self.DrawPlayer()

App()
