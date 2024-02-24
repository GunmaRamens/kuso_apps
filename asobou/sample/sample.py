from Asobou import Asobou

IMG_PATH = "./img/Monalisa.png"
IMG_NAME = "Monalisa"
SPACE_PX = 30

table = dict()
for index, char in enumerate(IMG_NAME):
    table[char] = index

# Todo: Classの中で文字を刻むべき
inali = [table[c] for c in "inali"]

asobou = Asobou(IMG_PATH, IMG_NAME)
image = asobou.gen_img_vertical(SPACE_PX, inali)
image.save("./img/inali.png")
