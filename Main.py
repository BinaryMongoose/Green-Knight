import pyxel
from player import Player 

class App():
    def __init__(self):
        # Initiate Window
        pyxel.init(128, 88, "Green Knight")

        pyxel.load("greenknight.pyxres", True, True, False, False)

        global player
        player = Player(20, 20)
        
        # Run Application
        pyxel.run(self.Update, self.Draw)

    def Update(self):
        
        player.UpdateControls()

    def DrawMap(self) :
        # Drawing the tileset
        pyxel.bltm(0, 0, 0, 0, 0, 1200, 94)

    # Draws all objects listed every frame
    def Draw(self) :
        
        self.DrawMap()
        
        # Draws player every frame.
        player.Draw()
        



App()
