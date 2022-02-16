import pyxel
from player import Player 

class App():
    def __init__(self):
        # Initiate Window
        pyxel.init(128, 88, "Ya Ya's Game")

        pyxel.load("greenknight.pyxres", True, True, False, False)

        global player
        player = Player(20, 20)
        
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
        



App()
