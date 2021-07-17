import cv2
import numpy as np 
from matplotlib import pyplot as plt 

bw = cv2.imread("trabalho4/bw.jpg")
cl = cv2.imread("trabalho4/cl.jpg")
cl = cv2.cvtColor(cl, cv2.COLOR_BGR2RGB)

plt.subplot(2, 2, 1), plt.imshow(bw, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.hist(bw.ravel(), 256, [0, 256]), plt.title("PRETO E BRANCO"), plt.xlim([0, 256]), plt.xticks([]), plt.yticks([])

cores = ('b', 'g', 'r')

plt.subplot(2, 2, 2), plt.imshow(cl), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.title("COLORIDA"), plt.xticks([]), plt.yticks([])

for i, col in enumerate(cores):
    histograma = cv2.calcHist([cl], [i], None, [256], [0, 256])
    plt.plot(histograma, color = col), plt.xlim([0, 256])

plt.show()