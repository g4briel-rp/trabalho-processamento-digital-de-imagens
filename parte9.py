import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def onChange(value):  
    pass

imagem = cv2.imread("trabalho9/img.jpg", 0)
copia = imagem.copy()

title = "LIMIARIZACAO COM TRACKBAR"
cv2.namedWindow(title)

cv2.createTrackbar("limiar", title, 0, 255, onChange)

valor_inicial = 0
alterar = False

while(True):
    valor_atual = cv2.getTrackbarPos("limiar", title)

    if valor_inicial != valor_atual:
        alterar = True
        valor_inicial = valor_atual

    if alterar == True:
        limiar, copia = cv2.threshold(imagem, valor_atual, 255, cv2.THRESH_BINARY)
        alterar = False

    cv2.imshow(title, copia)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()