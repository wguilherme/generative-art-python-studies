# import Image from pillow
from PIL import Image, ImageDraw
import random


def generateArt():
  print("Generating art...")
  imageSizePx = 128
  imageBgColor = (255, 255, 255)
  image = Image.new("RGB", 
  size=(imageSizePx, imageSizePx),
  color=imageBgColor)

  # draw basic lines
  draw = ImageDraw.Draw(image)

  for i in range(10):
    randomPoint1 = (
      random.randint(0, imageSizePx),
      random.randint(0, imageSizePx)
    )
    randomPoint2 = (
      random.randint(0, imageSizePx),
      random.randint(0, imageSizePx)
    )
    lineXy = (randomPoint1, randomPoint2)
    lineColor=(0,0,0)
    draw.line(lineXy, fill=(0,0,0), width=1)


  image.save('test.png')

if __name__ == "__main__":  #cannot run this file as a module/imported
  generateArt()
