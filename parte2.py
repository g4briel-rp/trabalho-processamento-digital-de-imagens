import cv2
import numpy as np 
from matplotlib import pyplot as plt

def maior(blue, green, red):
    if(blue > green):
        if(blue > red):
            return "a imagem é mais azul"
        else:
            return "a imagem é mais vermelha"
    elif(green > red):
        return "a imagem é mais verde"
    else:
        return "a imagem é mais vermelha"

dog = cv2.imread("trabalho2/cachorro.jpg")
dog = cv2.cvtColor(dog, cv2.COLOR_BGR2RGB)
altura, largura, _ = dog.shape

r, g, b = cv2.split(dog)

plt.subplot(1, 3, 1), plt.imshow(b, cmap="gray"), plt.title("BLUE"), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(g, cmap="gray"), plt.title("GREEN"), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(r, cmap="gray"), plt.title("RED"), plt.xticks([]), plt.yticks([])

blue  = 0
green = 0
red   = 0

for y in range(altura):
    for x in range(largura):
        blue  += dog.item(y, x, 2)
        green += dog.item(y, x, 1)
        red   += dog.item(y, x, 0)

blue  = blue/(altura*largura)
green = green/(altura*largura)
red   = red/(altura*largura)

print(maior(blue, green, red))

plt.show()