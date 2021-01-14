from skimage import feature

class HOG:
	def __init__(self, orientations = 9, pixelsPerCell = (8, 8),
		cellsPerBlock = (3, 3), transform = False):
		# armazena o número de orientações, pixels por célula
		self.orienations = orientations
		self.pixelsPerCell = pixelsPerCell
		self.cellsPerBlock = cellsPerBlock
		self.transform = transform

	def describe(self, image):
		# calcular HOG para a imagem
		hist = feature.hog(image, orientations = self.orienations,
			pixels_per_cell = self.pixelsPerCell,
			cells_per_block = self.cellsPerBlock,
			transform_sqrt = self.transform)

		return hist
        