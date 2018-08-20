from PIL import Image
import random

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

def randomGrid(im):
    ''' Shuffles picture into 36 parts '''
    (width, height) = im.size
    ptW = width//6
    ptH = height//6
    
    grid = [((0, ptW),(0, ptH)),      ((ptW, 2*ptW), (0, ptH)),       ((2*ptW, 3*ptW), (0, ptH)),      ((3*ptW, 4*ptW), (0, ptH)),       ((4*ptW, 5*ptW), (0, ptH)),       ((5*ptW, width), (0, ptH)),
            ((0, ptW),(ptH, 2*ptH)),  ((ptW, 2*ptW), (ptH, 2*ptH)),   ((2*ptW, 3*ptW), (ptH, 2*ptH)),  ((3*ptW, 4*ptW), (ptH, 2*ptH)),   ((4*ptW, 5*ptW), (ptH, 2*ptH)),   ((5*ptW, width), (ptH, 2*ptH)),
            ((0,ptW), (2*ptH, 3*ptH)),((ptW, 2*ptW), (2*ptH, 3*ptH)), ((2*ptW,3*ptW), (2*ptH, 3*ptH)), ((3*ptW, 4*ptW), (2*ptH, 3*ptH)), ((4*ptW, 5*ptW), (2*ptH, 3*ptH)), ((5*ptW, width), (2*ptH, 3*ptH)),
            ((0,ptW), (3*ptH, 4*ptH)),((ptW, 2*ptW), (3*ptH, 4*ptH)), ((2*ptW,3*ptW), (3*ptH, 4*ptH)), ((3*ptW, 4*ptW), (3*ptH, 4*ptH)), ((4*ptW, 5*ptW), (3*ptH, 4*ptH)), ((5*ptW, width), (3*ptH, 4*ptH)),
            ((0,ptW), (4*ptH, 5*ptH)),((ptW, 2*ptW), (4*ptH, 5*ptH)), ((2*ptW,3*ptW), (4*ptH, 5*ptH)), ((3*ptW, 4*ptW), (4*ptH, 5*ptH)), ((4*ptW, 5*ptW), (4*ptH, 5*ptH)), ((5*ptW, width), (4*ptH, 5*ptH)),
            ((0,ptW), (5*ptH, 6*ptH)),((ptW, 2*ptW), (5*ptH, 6*ptH)), ((2*ptW,3*ptW), (5*ptH, 6*ptH)), ((3*ptW, 4*ptW), (5*ptH, 6*ptH)), ((4*ptW, 5*ptW), (5*ptH, 6*ptH)), ((5*ptW, width), (5*ptH, 6*ptH))]
    shuffled = grid.copy()
    random.shuffle(shuffled)

    holdIm = Image.new('RGB', ( width//6, height//6))
    newIm  = Image.new('RGB', ( width, height))

    # Loop over the entire image
    for ind, block in enumerate(shuffled):
        for x in range(block[0][0], block[0][1]):
            for y in range(block[1][0], block[1][1]):
                (red, green, blue) = im.getpixel((x, y))

                holdIm.putpixel((x - block[0][0], y - block[1][0]), (red, green, blue))
        newIm.paste(holdIm, box=(grid[ind][0][0], grid[ind][1][0]))
    
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

bearBlur = blur(bear)
bearBlur.show()

bearShuffle = randomGrid(bear)
bearShuffle.show()
