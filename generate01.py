from PIL import Image, ImageDraw, ImageChops
import os
import random
import colorsys
import argparse


def randomPoint(imageSizePx: int, padding: int):
    return random.randint(padding, imageSizePx - padding)


def randomColor():

    # I want a bright, vivid color, so max V and S and only randomize HUE.
    h = random.random()
    s = 1
    v = 1
    floatRgb = colorsys.hsv_to_rgb(h, s, v)

    # Return as integer RGB.
    return (
        int(floatRgb[0] * 255),
        int(floatRgb[1] * 255),
        int(floatRgb[2] * 255),
    )


def interpolate(startColor, endColor, factor: float):
    # Find the color that is exactly factor (0.0 - 1.0) between the two colors.
    newColorRgb = []
    for i in range(3):
        newColorValue = factor * endColor[i] + (1 - factor) * startColor[i]
        newColorRgb.append(int(newColorValue))

    return tuple(newColorRgb)


def generateArt(collection: str, name: str):
    print("Generating art")

    # Figure out where we are going to put it.
    outputDir = os.path.join("output", collection)
    imagePath = os.path.join(outputDir, f"{name}.png")

    # Set size parameters.
    rescale = 2
    imageSizePx = 128 * rescale
    padding = 12 * rescale

    # Create the directory and base image.
    os.makedirs(outputDir, exist_ok=True)
    bg_color = (0, 0, 0)
    image = Image.new("RGB", (imageSizePx, imageSizePx), bg_color)

    # How many lines do we want to draw?
    numLines = 10
    points = []

    # Pick the colors.
    startColor = randomColor()
    endColor = randomColor()

    # Generate points to draw.
    for _ in range(numLines):
        point = (
            randomPoint(imageSizePx, padding),
            randomPoint(imageSizePx, padding),
        )
        points.append(point)

    # Center image.
    # Find the bounding box.
    minX = min([p[0] for p in points])
    maxX = max([p[0] for p in points])
    minY = min([p[1] for p in points])
    maxY = max([p[1] for p in points])

    # Find offsets.
    xOffset = (minX - padding) - (imageSizePx - padding - maxX)
    yOffset = (minY - padding) - (imageSizePx - padding - maxY)

    # Move all points by offset.
    for i, point in enumerate(points):
        points[i] = (point[0] - xOffset // 2, point[1] - yOffset // 2)

    # Draw the points.
    currentThickness = 1 * rescale
    nPoints = len(points) - 1
    
    
    for i, point in enumerate(points):

        # Create the overlay.
        draw = ImageDraw.Draw(image)
        # overlayImage = Image.new("RGB", (imageSizePx, imageSizePx), (0, 0, 0))
        # overlayImage = Image.new("RGB", (imageSizePx, imageSizePx), (0, 0, 0))
        # overlayDraw = ImageDraw.Draw(overlayImage)

        if i == nPoints:
            # Connect the last point back to the first.
            nextPoint = points[0]
        else:
            # Otherwise connect it to the next element.
            nextPoint = points[i + 1]

        # Find the right color.
        factor = i / nPoints
        lineColor = interpolate(startColor, endColor, factor=factor)

        # Draw the line.
        draw.line([point, nextPoint], fill=lineColor, width=currentThickness)
        # overlayDraw.line([point, nextPoint], fill=lineColor, width=currentThickness)

        # Increase the thickness.
        currentThickness += rescale

        # Add the overlay channel.
        # image = ImageChops.add(image, overlayImage)

    # Image is done! Now resize it to be smooth.
    image = image.resize(
        (imageSizePx // rescale, imageSizePx // rescale), resample=Image.ANTIALIAS
    )

    # Save the image.
    image.save(imagePath)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int, default=1, help="Number of images to generate.")
    parser.add_argument("--collection", type=str, help="Collection name for the art.")

    args = parser.parse_args()
    n = args.n
    # collectionName = args.collection
    collectionName = 'generative01'

    for i in range(n):
        generateArt(collectionName, f"{collectionName}_image_{i}")