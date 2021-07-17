import cv2
import numpy as np
from matplotlib import pyplot as plt 

def compara(S1, S2, D1, D2, D3):

    hist_S1 = cv2.calcHist([S1], [0], None, [256], [0, 256])
    hist_S2 = cv2.calcHist([S2], [0], None, [256], [0, 256])
    hist_D1 = cv2.calcHist([D1], [0], None, [256], [0, 256])
    hist_D2 = cv2.calcHist([D2], [0], None, [256], [0, 256])
    hist_D3 = cv2.calcHist([D3], [0], None, [256], [0, 256])

    #correl: mais proximo de 1 
    #chisqr: mais proximo de 0
    #bhatta: mais proximo de 0

    Correl = np.array([cv2.compareHist(hist_S1, hist_S1, cv2.HISTCMP_CORREL), cv2.compareHist(hist_S1, hist_S2, cv2.HISTCMP_CORREL), 
    cv2.compareHist(hist_S1, hist_D1, cv2.HISTCMP_CORREL), cv2.compareHist(hist_S1, hist_D2, cv2.HISTCMP_CORREL), cv2.compareHist(hist_S1, hist_D3, cv2.HISTCMP_CORREL)])

    Chisqr = np.array([cv2.compareHist(hist_S1, hist_S1, cv2.HISTCMP_CHISQR), cv2.compareHist(hist_S1, hist_S2, cv2.HISTCMP_CHISQR), 
    cv2.compareHist(hist_S1, hist_D1, cv2.HISTCMP_CHISQR), cv2.compareHist(hist_S1, hist_D2, cv2.HISTCMP_CHISQR), cv2.compareHist(hist_S1, hist_D3, cv2.HISTCMP_CHISQR)])

    Bhatta = np.array([cv2.compareHist(hist_S1, hist_S1, cv2.HISTCMP_BHATTACHARYYA), cv2.compareHist(hist_S1, hist_S2, cv2.HISTCMP_BHATTACHARYYA),
    cv2.compareHist(hist_S1, hist_D1, cv2.HISTCMP_BHATTACHARYYA), cv2.compareHist(hist_S1, hist_D2, cv2.HISTCMP_BHATTACHARYYA), cv2.compareHist(hist_S1, hist_D3, cv2.HISTCMP_BHATTACHARYYA)])
    
    plt.figure()
    plt.suptitle("CORRELAÇÃO", fontsize = 20)
    plt.subplot(2, 5, 1), plt.imshow(S1, cmap='gray'), plt.title("%.5f" % (Correl[0])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 2), plt.imshow(S2, cmap='gray'), plt.title("%.5f" % (Correl[1])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 3), plt.imshow(D1, cmap='gray'), plt.title("%.5f" % (Correl[2])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 4), plt.imshow(D2, cmap='gray'), plt.title("%.5f" % (Correl[3])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 5), plt.imshow(D3, cmap='gray'), plt.title("%.5f" % (Correl[4])), plt.xticks([]), plt.yticks([])

    plt.figure()
    plt.suptitle("CHI-SQUARE", fontsize = 20)
    plt.subplot(2, 5, 1), plt.imshow(S1, cmap='gray'), plt.title("%.1f" % (Chisqr[0])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 2), plt.imshow(S2, cmap='gray'), plt.title("%.1f" % (Chisqr[1])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 3), plt.imshow(D1, cmap='gray'), plt.title("%.1f" % (Chisqr[2])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 4), plt.imshow(D2, cmap='gray'), plt.title("%.1f" % (Chisqr[3])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 5), plt.imshow(D3, cmap='gray'), plt.title("%.1f" % (Chisqr[4])), plt.xticks([]), plt.yticks([])

    plt.figure()
    plt.suptitle("BHATTACHARYYA", fontsize = 20)
    plt.subplot(2, 5, 1), plt.imshow(S1, cmap='gray'), plt.title("%.5f" % (Bhatta[0])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 2), plt.imshow(S2, cmap='gray'), plt.title("%.5f" % (Bhatta[1])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 3), plt.imshow(D1, cmap='gray'), plt.title("%.5f" % (Bhatta[2])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 4), plt.imshow(D2, cmap='gray'), plt.title("%.5f" % (Bhatta[3])), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 5), plt.imshow(D3, cmap='gray'), plt.title("%.5f" % (Bhatta[4])), plt.xticks([]), plt.yticks([])


imagem1 = cv2.imread("trabalho7/cachorro.jpg")
imagem1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)

imagem2 = cv2.imread("trabalho7/cachorro2.jpg")
imagem2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

imagem3 = cv2.imread("trabalho7/pato.jpg")
imagem3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY)

imagem4 = cv2.imread("trabalho7/dinossauro.jpg")
imagem4 = cv2.cvtColor(imagem4, cv2.COLOR_BGR2GRAY)

imagem5 = cv2.imread("trabalho7/macaco.jpg")
imagem5 = cv2.cvtColor(imagem5, cv2.COLOR_BGR2GRAY)

altura, largura = imagem2.shape

imagem1 = cv2.resize(imagem1, (largura, altura))
imagem3 = cv2.resize(imagem3, (largura, altura))
imagem4 = cv2.resize(imagem4, (largura, altura))
imagem5 = cv2.resize(imagem5, (largura, altura))

compara(imagem1, imagem2, imagem3, imagem4, imagem5)

plt.show()