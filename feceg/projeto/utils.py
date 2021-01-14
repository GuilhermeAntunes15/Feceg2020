from django.conf import settings
from .pyrobocity.descriptor import HOG
from .pyrobocity.preprocessing import Deskew,CenterExtent
from sklearn.externals import joblib
import numpy as np
import imutils
import mahotas
import cv2
import os 

deskew = Deskew(20)
center_extent = CenterExtent((20,20))
preprocessors = [deskew,center_extent]

hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
	cellsPerBlock = (1, 1), transform = True)


model = joblib.load(os.path.join(settings.PROTECTED_MEDIA_ROOT,"svm.cpickle"))

def auto_canny(image, sigma=0.33):
	# calcula a mediana das intensidades de pixel de canal único
	v = np.median(image)
 
	# aplique a detecção automática de borda Canny usando a mediana calculada
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# retornar a imagem com arestas
	return edged

def recognize(image):
	output = list()
	image = imutils.resize(image,width=500)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = auto_canny(image)
	cv2.imwrite("edged.png",edged)
	(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	cv2.drawContours(edged, cnts, -1, (0,255,0), 3)
	(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])
	
	print("Contours",len(cnts))
	for (c,_) in cnts:
		cv2.drawContours(image, [c], 0, (0,255,0), 3)
		cv2.imwrite("drawContours.png",image)
		(x,y,w,h) = cv2.boundingRect(c)
	 
		roi = gray[y:y+h,x:x+w]
		thresh = roi.copy()
		T = mahotas.thresholding.otsu(roi)
		thresh[thresh > T] = 255
		thresh = cv2.bitwise_not(thresh)

		for preprocessor in preprocessors:
			thresh = preprocessor.preprocess(thresh)

		hist = hog.describe(thresh)
		hist = hist.reshape(1,-1)
		digit = model.predict(hist)[0]
		print("O numero é: {}".format(digit))
		output.append(str(digit))

	return output
