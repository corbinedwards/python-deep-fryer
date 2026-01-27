import os, sys, shutil
from PIL import Image, ImageEnhance

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

def SaveImage(img, lofi = False):
	global iteration
	pathToUpdate = dirName + "/" + saveName + str(iteration) + ".jpg"
	if lofi:
		img.save(pathToUpdate, quality=1)
	else:
		img.save(pathToUpdate)
	iteration = iteration + 1
	return pathToUpdate

imagePath = sys.argv[1]
saveName = sys.argv[2]
dirName = saveName + " Fries"
iteration = 1

if os.path.exists(dirName):
	shutil.rmtree(dirName)
	os.mkdir(dirName)
else:
	os.mkdir(dirName)


#First Image
im = Image.open(imagePath)
updated = SaveImage(im)

#Second Image
im = Image.open(updated)
im = ContrastImage(im, 2)
updated = SaveImage(im)

#Third Image
im = Image.open(imagePath)
#im = SaturateImage(im, 5)
im = SharpenImage(im, 10)
updated = SaveImage(im)

#Fourth Image
im = Image.open(updated)
im = ContrastImage(im, 2)
updated = SaveImage(im, True)

#Fifth Image
im = Image.open(updated)
#im = SaturateImage(im, 5)
im = SharpenImage(im, 5)
im = ContrastImage(im, 2)
updated = SaveImage(im)
