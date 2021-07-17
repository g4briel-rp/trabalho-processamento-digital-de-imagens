import cv2
import numpy as np
from matplotlib import pyplot as plt 

def crop(imagem, x, y, altura, largura):
    pedaco = imagem[y:y+altura, x:x+largura]
    return pedaco

def paste(imagem, imagem_destino, x, y):
    imagem_destino[y:y+imagem.shape[0], x:x+imagem.shape[1]] = imagem
    return imagem_destino

fred = cv2.imread("trabalho1/fred.jpg")
fred = cv2.cvtColor(fred, cv2.COLOR_BGR2RGB)

x_bola = 385
y_bola = 443
altura_bola = 58
largura_bola = 71

bola = crop(fred, x_bola, y_bola, altura_bola, largura_bola)

x_destino = 525
y_destino = 443

nova_imagem = paste(bola, fred, x_destino, y_destino)

plt.imshow(nova_imagem), plt.xticks([]), plt.yticks([])
plt.show()