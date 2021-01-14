from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from PIL import Image
import imutils
import io
import cv2
import re
import numpy as np
import base64

from projeto import utils_shape


# Take in base64 string and return cv image
def stringToRGB(base64_string):
    dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
    image_data = base64_string
    image_data = dataUrlPattern.match(image_data).group(2)
    image_data = image_data.encode()
    image_data = base64.b64decode(image_data)
    image_data = Image.open(io.BytesIO(image_data))
    image = cv2.cvtColor(np.array(image_data), cv2.COLOR_BGR2RGB)
    return image


@csrf_exempt
def shape(request):
	if request.method == 'POST':
		image = stringToRGB(request.POST.get('image'))
		outputs = utils_shape.recognize(image)
		outputs = ",".join(outputs)
		return JsonResponse({'output': outputs})

	return render(request, 'shapes.html', {})
