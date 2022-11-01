import pyxel as pyx

print("Hello!")

class Player():
    def __init__(self):
        # Player variables
        self.x = 50
        self.y = 50

        # 1 for right, 0 for left
        self.direction = 0

        self.vel = 4
        self.jumpheight = 5

        # Flags for keypresses
        self.leftDown   = False
        self.rightDown  = False
        self.haveJumped = False

        pyx.load("../Assets/greenknight.pyxres")
    
    def Draw(self):
        pyx.blt(self.x, self.y, 1, 8, 0, 8, 16, 0)
    
    def Update(self):
        self.Draw()
        self.UpdateControls()
        print(self.x)

    def Move(self):
        UpdateControls()
        if self.leftDown:
            self.x += self.vel

        if self.rightDown:
            self.y -= self.vel

    
    def UpdateControls(self):
        if pyx.btnp(pyx.KEY_D):
            self.rightDown = True
   
        if pyx.btnp(pyx.KEY_A):
            self.leftDown = True
    
        if pyx.btnr(pyx.KEY_D):
            self.rightDown = False

        if pyx.btnr(pyx.KEY_A):
            self.leftDown = False



class App():
    """ The main class """
    def __init__(self):
        pyx.init(100, 100, "Green Knight")
        pyx.load("../Assets/greenknight.pyxres")
        
        self.p = Player()

        pyx.run(self.update, self.draw)

    def update(self):
        self.p.Update()

    def draw(self):
        pass
               
App()
