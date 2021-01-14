import imutils 
import numpy as np
import cv2

class Deskew:
    def __init__(self,width):
        self.width = width
    
    def preprocess(self,image):
        # agarre a largura e a altura da imagem e calcule
        (h, w) = image.shape[:2]
        moments = cv2.moments(image)

        # alinhar a imagem aplicando uma transformação afim
        skew = moments["mu11"] / moments["mu02"]

        M = np.float32([
        [1, skew, -0.5 * w * skew],
        [0, 1, 0]])
        image = cv2.warpAffine(image, M, (w, h),
        flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)

        # redimensionar a imagem para ter uma largura constante
        image = imutils.resize(image, width = self.width)

        return image

