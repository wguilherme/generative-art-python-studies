# import Image from pillow
from PIL import Image


def generateArt():
  print("Generating art...")
  image = Image.new("RGB", (128, 128))
  image.save('test.png')

if __name__ == "__main__":  #cannot run this file as a module/imported
  generateArt()
