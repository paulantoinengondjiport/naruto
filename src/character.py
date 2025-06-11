from PIL import Image
from imageframe import ImageFrame
class Character:
    
    def __init__(self,data,scale):
        self.name = data["name"]
        self.attributes = [data["ninjutsu"], data["genjutsu"], data["taijutsu"],
                           data["battle_iq"], data["kekkei_genkai"], data["chakra_type"]]
        self.img = ImageFrame("../img/" + self.name + ".png", scale)
        self.isPressed = False
    
    