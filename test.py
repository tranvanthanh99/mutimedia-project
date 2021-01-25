from PIL import Image

img = Image.open('lena.png').convert('LA')
img.save('greyscale.png')