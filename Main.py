import pyxel
from player import Player

FLOOR_TILE = (5, 0)
TORCH_TILE = (3, 0)
FLOOR_TILE_BOX = (5, 1)

TORCH_TILES = [(1, 0), (2, 0), (3, 0), (4, 0)]

COLLIDE_X = 5


def getTile(x, y):
    return pyxel.tilemap(0).pget(x, y)


def updateMap():
    for currentX in range(0, 16):
        for currentY in range(0, 10):
            currentTile = getTile(currentX, currentY)

            # if currentTile[0] >= COLLIDE_X:
            #     pyxel.tilemap(0).pset(currentX, currentY, FLOOR_TILE_BOX)

            if currentTile in TORCH_TILES:
                u = ((pyxel.frame_count // 6 % 4) + 1) * 1
                drawTile = (u, 0)
                pyxel.tilemap(0).pset(currentX, currentY, drawTile)


# noinspection PyGlobalUndefined
class App:
    def __init__(self):
        # Initiate Window
        # noinspection PyArgumentList
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
        updateMap()

    # Draws all objects listed every frame
    def Draw(self):
        self.DrawMap()
        player.Draw()

        # pyxel.text(5, 70, , 7)


App()
