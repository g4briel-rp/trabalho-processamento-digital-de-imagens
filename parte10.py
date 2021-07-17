import cv2
import numpy as np 
from matplotlib import pyplot as plt

def aplicar(imagem, filtro):
    copia = imagem.copy()
    aux   = imagem.copy()

    if(filtro == "Media"):
        copia = cv2.blur(imagem, [5, 5])
    elif(filtro == "Gaussiano"):
        copia = cv2.GaussianBlur(imagem, (5, 5), 0)
    elif(filtro == "Mediana"):
        copia = cv2.medianBlur(imagem, 5)
    elif(filtro == "Sobel"):
        copia = cv2.cvtColor(copia, cv2.COLOR_RGB2GRAY)
        copiaH = cv2.Sobel(copia, 5, 1, 0)
        copiaV = cv2.Sobel(copia, 5, 0, 1)
        copia = copiaH + copiaV
    elif(filtro == "Laplaciano"):
        aux = cv2.cvtColor(aux, cv2.COLOR_RGB2GRAY)
        copia = cv2.cvtColor(copia, cv2.COLOR_RGB2GRAY)
        copia = cv2.Laplacian(copia, cv2.CV_64F, 5)
        copia = copia + aux
        copia = cv2.convertScaleAbs(copia)
    
    return copia

filtros = ["Media", "Gaussiano", "Mediana", "Sobel", "Laplaciano"]

natureza = cv2.imread("trabalho10/ruido.jpg")
natureza = cv2.cvtColor(natureza, cv2.COLOR_BGR2RGB)

altura, largura, _ = natureza.shape
resultado = np.zeros([largura, altura])

plt.imshow(natureza), plt.title("ORIGINAL"), plt.xticks([]), plt.yticks([])

for x in range(1, 6):
    resultado = aplicar(natureza, filtros[x-1])

    if(filtros[x-1] == "Laplaciano" or filtros[x-1] == "Sobel"):
        plt.figure(), plt.imshow(resultado, cmap='gray'), plt.title(filtros[x-1]), plt.xticks([]), plt.yticks([])
    else:
        plt.figure(), plt.imshow(resultado), plt.title(filtros[x-1]), plt.xticks([]), plt.yticks([])

plt.show()