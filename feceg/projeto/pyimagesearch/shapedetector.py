import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# inicialize o nome da forma e aproxime o contorno
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		#se a forma for um triângulo, ela terá 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		# se a forma tiver 4 vértices é um quadrado ou se nao é
		# um rectângulo
		elif len(approx) == 4:
			# calcule um limite do contorno e use o
			# limite para calcular a proporção
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# um quadrado terá uma proporção aproximada
			# igual a um, caso contrário, a forma é um retângulo
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		#se tiver 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"

		else:
			shape = "circle"

		# retorna o nome da forma
		return shape