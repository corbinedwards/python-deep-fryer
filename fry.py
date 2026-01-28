import os
import shutil
from PIL import Image, ImageEnhance
from pathlib import Path


def SaturateImage(img, rate):
    saturate = ImageEnhance.Color(img)
    imgSaturated = saturate.enhance(rate)
    return imgSaturated


def SharpenImage(img, rate):
    sharpen = ImageEnhance.Sharpness(img)
    imgSharpened = sharpen.enhance(rate)
    return imgSharpened


def ContrastImage(img, rate):
    contrast = ImageEnhance.Contrast(img)
    imgContrasted = contrast.enhance(rate)
    return imgContrasted


def SaveImage(img, lofi=False):
    global iteration
    pathToUpdate = savePath + "/" + str(iteration) + ".jpg"
    if lofi:
        img.save(pathToUpdate, quality=1)
    else:
        img.save(pathToUpdate)
    iteration = iteration + 1
    return pathToUpdate


imagePath = input("Enter path of image to fry: ")
if not os.path.exists(imagePath):
    print("Error: image not found")
    exit(0)

savePath = input("Enter path for fried images: ")
if not os.path.exists(savePath):
    print("Error: save path not found")
    exit(0)

# Create directory name from image
imageName = Path(imagePath).stem
savePath = savePath + "/" + imageName + "-fries"
iteration = 1

# Delete save directory if it already exists:
if os.path.exists(savePath):
    removeDirectory = input(
        "Directory '"
        + savePath
        + "' already exists. Do you want to override and delete everything inside it? [y/n]: "
    )
    if removeDirectory == "y":
        shutil.rmtree(savePath)
    else:
        exit(0)

os.mkdir(savePath)

# First Image
img = Image.open(imagePath)
updated = SaveImage(img)

# Second Image
img = Image.open(updated)
img = ContrastImage(img, 2)
updated = SaveImage(img)

# Third Image
img = Image.open(imagePath)
# im = SaturateImage(im, 5)
img = SharpenImage(img, 10)
updated = SaveImage(img)

# Fourth Image
img = Image.open(updated)
img = ContrastImage(img, 2)
updated = SaveImage(img, True)

# Fifth Image
img = Image.open(updated)
# im = SaturateImage(im, 5)
img = SharpenImage(img, 5)
img = ContrastImage(img, 2)
updated = SaveImage(img)

print()
print("Success! Images saved to " + savePath)
