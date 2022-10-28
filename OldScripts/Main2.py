import pyxel as pyx
from player import Player

FLOOR_TILE = (5, 0)
TORCH_TILE = (3, 0)
FLOOR_TILE_BOX = (5, 1)

TORCH_TILES = [(1, 0), (2, 0), (3, 0), (4, 0)]
COLLIDE_X = 5
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 88


def getTile(x, y):
    """ Gets a tile from the displayed tile-map and returns the tile's x and y from the image bank """
    return pyx.tilemap(0).pget(x, y)


def updateMap():
    """ Finds specific tiles off the map and animates the tiles """
    for currentX in range(0, int(SCREEN_WIDTH / 8)):
        for currentY in range(0, int(SCREEN_HEIGHT / 8)):
            currentTile = getTile(currentX, currentY)

            if currentTile in TORCH_TILES:
                u = ((pyx.frame_count // 6 % 4) + 1)
                drawTile = (u, 0)
                pyx.tilemap(0).pset(currentX, currentY, drawTile)


class App:
    """ The main game """

    def __init__(self):
        """ Contains all code for the startup of the game """
        pyx.init(SCREEN_WIDTH, SCREEN_HEIGHT, "Green Knight")
        pyx.load("../Assets/greenknight.pyxres")

        global player
        player = Player(10, 32)

        # Run Application
        pyx.run(self.Update, self.Draw)

    def Update():
        """ Updates everything listed every frame, including input """
        player.UpdateControls()

    def DrawMap():
        """ Draws the tile-map """
