# import Image from pillow
from PIL import Image, ImageDraw
import random

def randomColor():
  return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def generateArt():
  print("Generating art...")
  imageSizePx = 128
  paddingPx = 16
  imageBgColor = (255, 255, 255)
  image = Image.new("RGB", 
  size=(imageSizePx, imageSizePx),
  color=imageBgColor)

  # draw basic lines
  draw = ImageDraw.Draw(image)
  points =[]
  
  # Generate the points.
  for i in range(10):
    randomPoint = (
      random.randint(paddingPx, imageSizePx-paddingPx),
      random.randint(paddingPx, imageSizePx-paddingPx),
    )
    points.append(randomPoint)

  # Draw the points.
  thickness=0
  for i, point in enumerate(points):
    point1 = point
    
    if i == len(points) -1:
      point2 = points[0]
    else:
      point2 = points[i+1]
    

    lineXy = (point1, point2)
    lineColor=randomColor()
    thickness+=1
    draw.line(lineXy, fill=lineColor, width=thickness)


  image.save('test.png')

if __name__ == "__main__":  #cannot run this file as a module/imported
  generateArt()
