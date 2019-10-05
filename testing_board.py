import numpy
from PIL import Image

data = numpy.zeros((1024, 1024, 3), dtype=numpy.uint8)
data[512, 511] = [255, 0, 0]
data[512, 512] = [0, 255, 0]
data[512, 513] = [0, 0, 255]

for i in range(0,255):
    for j in range(1024):
        data[i][j] = [255, 0, 0]
        data[i+256][j] = [0, 255, 0]
        data[i+512][j] = [0, 0, 255]

image = Image.fromarray(data)
image.show()
