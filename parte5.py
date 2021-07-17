import cv2
import numpy as np
from matplotlib import pyplot as plt 

campo = cv2.imread(("trabalho5/campo.jpg"))
marca = cv2.imread(("trabalho5/marca.png"))
campo = cv2.cvtColor(campo, cv2.COLOR_BGR2RGB)
marca = cv2.cvtColor(marca, cv2.COLOR_BGR2RGB)

Image = cv2.addWeighted(campo, 0.8, marca, 0.2, 0.0)

plt.imshow(Image), plt.xticks([]), plt.yticks([])
plt.show()