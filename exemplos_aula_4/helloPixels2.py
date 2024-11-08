import numpy as np
import cv2 as cv

img = cv.imread('rgb.png')
img_result = img.copy()

print(img.shape) # (512, 512, 3) -> (altura, largura, canais_cor) retorna infos da foto.
# PNG não necessariamente usa os 4 canais, caso da aula, que era .png e tinha 3 canais.
# canal vai estar codificado em b,g,r (específico do opencv)

for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    img.item(i, j, 0) # (indice_linha, indice_coluna, indice_canal)
    #media = (img.item(i, j, 0) + img.item(i, j, 1) + img.item(i, j, 2)) / 3
    img_result[i][j][0] = img.item(i, j, 1)
    img_result[i][j][1] = img.item(i, j, 1)
    img_result[i][j][2] = img.item(i, j, 1)
    #img_result.itemset((i, j, 0), media) # canal B
    #img_result.itemset((i, j, 1), media) # canal G
    #img_result.itemset((i, j, 2), media) # canal R



cv.imshow('Hello OpenCV', img_result)

k = cv.waitKey(0)