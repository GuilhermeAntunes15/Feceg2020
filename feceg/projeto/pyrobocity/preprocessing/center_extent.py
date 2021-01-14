import imutils
import mahotas
import numpy as np 
import cv2

class CenterExtent:
    def __init__(self,size):
        self.size = size 
    

    def preprocess(self,image):
        # pegue a extensão da largura e altura
        (eW, eH) = self.size

        # manipular quando a largura for maior que a altura
        if image.shape[1] > image.shape[0]:
            image = imutils.resize(image, width = eW)

        # caso contrário, a altura é maior que a largura
        else:
            image = imutils.resize(image, height = eH)


        extent = np.zeros((eH, eW), dtype = "uint8")
        offsetX = (eW - image.shape[1]) // 2
        offsetY = (eH - image.shape[0]) // 2
        extent[offsetY:offsetY + image.shape[0], offsetX:offsetX + image.shape[1]] = image

        # calcular o centro de massa da imagem e depois
        # mova o centro de massa para o centro da imagem
        (cY, cX) = np.round(mahotas.center_of_mass(extent)).astype("int32")
        (dX, dY) = ((self.size[0] // 2) - cX, (self.size[1] // 2) - cY)
        M = np.float32([[1, 0, dX], [0, 1, dY]])
        extent = cv2.warpAffine(extent, M, self.size)

        # retornar a extensão da imagem
        return extent