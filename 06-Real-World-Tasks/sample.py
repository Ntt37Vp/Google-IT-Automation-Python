from PIL import Image

im = Image.open("bridge.jpg")
im.rotate(45).show()
