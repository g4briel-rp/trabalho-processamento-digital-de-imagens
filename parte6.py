import cv2
import numpy as np
from matplotlib import pyplot as plt 

tigre = cv2.imread("trabalho6/tigre.jpg", 0)
eqHist = cv2.equalizeHist(tigre)

plt.subplot(2, 2, 1), plt.imshow(tigre, cmap="gray"), plt.title("IMAGEM ORIGINAL"), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(eqHist, cmap="gray"), plt.title("IMAGEM EQUALIZADA"), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.hist(tigre.ravel(), 256, [0, 256]), plt.title("HISTOGRAMA ORIGINAL"), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.hist(eqHist.ravel(), 256, [0, 256]), plt.title("HISTOGRAMA EQUALIZADO"), plt.xticks([]), plt.yticks([])

plt.show()