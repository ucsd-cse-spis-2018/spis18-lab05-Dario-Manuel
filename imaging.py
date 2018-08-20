from PIL import Image

def grayscale(im):
    ''' Create grayscale image from im object '''
    # Find the dimensions of im object
    (width, height) = im.size

    # Loop over picture
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x,y))

            luminance = int(red*.21 + green*.72 + blue*.07)
            im.putpixel((x, y), (luminance, luminance, luminance))

def binarize(im, thresh, startx, starty, endx, endy):
    ''' Create binarized image in certain part of a picture '''
    # Find the dimensions of im object
    (width, height) = im.size

    if startx < 0 or starty < 0:
        print("Start size is too small! Please try again.")
        return
    elif endx > width or endy > height:
        print("End size is too large! Please try again.")
        return

    # Loop over picture
    for x in range(startx, endx):
        for y in range(starty, endy):
            (red, green, blue) = im.getpixel((x,y))

            luminance = int(red*.21 + green*.72 + blue*.07)

            if luminance >= thresh:
                im.putpixel((x,y), (255, 255, 255))
            else:
                im.putpixel((x,y), (0, 0, 0))

def mirrorVert(im):
    ''' Make mirror image of top of a picture '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(0, height//2):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel((x, height - y - 1), (red, green, blue))

def mirrorHoriz(im):
    ''' Make mirror image of left of a picture '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(0, width//2):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel((width - x - 1, y), (red, green, blue))

def flipVert(im):
    ''' Make mirror image of top of a picture '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(0, height//2):
            (red, green, blue) = im.getpixel((x, y))
            (red2, green2, blue2) = im.getpixel((x, height - y - 1))


            im.putpixel((x, height - y - 1), (red, green, blue))
            im.putpixel((x, y), (red2, green2, blue2))


def scale(im):
    ''' Make mirror image of left of a picture '''
    # Find the dimensions of the image
    (width, height) = im.size
    newIm  = Image.new('RGB', ( width//2, height//2))

    # Loop over the entire image
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))

            newIm.putpixel((x//2, y//2), (red, green, blue))
    return newIm
            
def blur(im):
    ''' Make mirror image of left of a picture '''
    # Find the dimensions of the image
    (width, height) = im.size
    newIm  = Image.new('RGB', ( width, height))

    # Loop over the entire image
    for x in range(1, width - 1, 2):
        for y in range(1, height - 1, 2):
            (redNW, greenNW, blueNW) = im.getpixel((x-1, y-1))
            (redN, greenN, blueN) = im.getpixel((x, y-1))
            (redNE, greenNE, blueNE) = im.getpixel((x+1, y-1))
            (redW, greenW, blueW) = im.getpixel((x-1, y))
            (red, green, blue) = im.getpixel((x, y))
            (redE, greenE, blueE) = im.getpixel((x+1, y))
            (redSW, greenSW, blueSW) = im.getpixel((x-1, y+1))
            (redS, greenS, blueS) = im.getpixel((x, y+1))
            (redSE, greenSE, blueSE) = im.getpixel((x+1, y+1))

            newRed = (redNW + redN + redNE + redW + red + redE + redSW + redS + redSE) //9
            newGreen = (greenNW + greenN + greenNE + greenW + green + greenE + greenSW + greenS + greenSE) //9
            newBlue = (blueNW + blueN + blueNE + blueW + blue + blueE + blueSW + blueS + blueSE) //9


            newIm.putpixel((x-1, y-1), (newRed, newGreen, newBlue))
            newIm.putpixel((x, y-1), (newRed, newGreen, newBlue))
            newIm.putpixel((x+1, y-1), (newRed, newGreen, newBlue))
            newIm.putpixel((x-1, y), (newRed, newGreen, newBlue))
            newIm.putpixel((x, y), (newRed, newGreen, newBlue))
            newIm.putpixel((x+1, y), (newRed, newGreen, newBlue))
            newIm.putpixel((x-1, y+1), (newRed, newGreen, newBlue))
            newIm.putpixel((x, y+1), (newRed, newGreen, newBlue))
            newIm.putpixel((x+1, y+1), (newRed, newGreen, newBlue))
    return newIm
            









######################### FUNCTIONS DEFINED #########################

# Opens the "bear.jpg" file to RAM and creates a pointer to it at "bear"
bear = Image.open("bear.jpg")

# Displays the image that "bear" is pointing to
bear.show()
grayscale(bear)
bear.show()

# Resets bear
bear = Image.open("bear.jpg")

# Displays the image that "bear" is pointing to
binarize(bear, 100, 30, 30, 300, 390)
bear.show()
binarize(bear, 100, -30, 30, 90, 90)
binarize(bear, 100, 30, 30, 100090, 90)

# Resets bear
bear = Image.open("bear.jpg")
# Displays the image that "bear" is pointing to
mirrorVert(bear)
bear.show()

# Resets bear
bear = Image.open("bear.jpg")
# Displays the image that "bear" is pointing to
mirrorHoriz(bear)
bear.show()

# Resets bear
bear = Image.open("bear.jpg")
# Displays the image that "bear" is pointing to
flipVert(bear)
bear.show()

# Resets bear
bear = Image.open("bear.jpg")
bearScale= scale(bear)
bearScale.show()

# Resets bear
bearBlur = blur(bear)
bearBlur.show()
