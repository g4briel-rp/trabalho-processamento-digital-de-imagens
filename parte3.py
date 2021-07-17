import cv2
import numpy as np
from matplotlib import pyplot as plt 

thor = cv2.imread("trabalho3/thor.jpg")
thor = cv2.cvtColor(thor, cv2.COLOR_BGR2RGB)
loki = cv2.imread("trabalho3/loki.jpg")
loki = cv2.cvtColor(loki, cv2.COLOR_BGR2RGB)

thoki = cv2.addWeighted(thor, 0.5, loki, 0.5, 0.0)

plt.imshow(thoki), plt.xticks([]), plt.yticks([])

plt.show()