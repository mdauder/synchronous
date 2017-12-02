'''we areto achive overlapping of two given image so that NIR image and RGB image can be combined to get 
   NDVI IMAGE'''

import operator
from PIL import Image
from PIL import ImageDraw

# our first image is img1 and second image is img2 
img1 = Image.new('RGB', size=(100, 100), color=(255, 0, 0))
img2 = Image.new('RGB', size=(120, 130), color=(0, 255, 0))

shift = (50, 60)


nw, nh = map(max, map(operator.add, img2.size, shift), img1.size)


newimg1 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
newimg1.paste(img2, shift)
newimg1.paste(img1, (0, 0))


newimg2 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
newimg2.paste(img1, (0, 0))
newimg2.paste(img2, shift)

result = Image.blend(newimg1, newimg2, alpha=0.5)
