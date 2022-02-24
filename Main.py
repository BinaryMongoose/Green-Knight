import pyxel
from player import Player


# noinspection PyGlobalUndefined
class App:
    def __init__(self):
        # Initiate Window
        pyxel.init(128, 88, "Green Knight")

        pyxel.load("greenknight.pyxres")

        global player
        player = Player(10, 34)

        # Run Application
        pyxel.run(self.Update, self.Draw)

    @staticmethod
    def Update():
        player.UpdateControls()

    @staticmethod
    def DrawMap():
        # Drawing the tile-set
        pyxel.bltm(0, 0, 0, 0, 0, 1200, 94)

    # Draws all objects listed every frame
    def Draw(self):
        self.DrawMap()

        # Draws player every frame.
        player.Draw()

        pyxel.text(5, 70, str(player.leftDown), 7)
        pyxel.text(5, 80, str(player.rightDown), 7)

        pyxel.text(30, 70, str(player.dy), 7)
        pyxel.text(30, 80, str(player.dx), 7)


App()
