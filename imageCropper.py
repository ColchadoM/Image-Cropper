from PIL import Image

img = Image.open("image.jpg")

area = (1090,220,2810,1300)
cropped_img = img.crop(area)

cropped_img.show()