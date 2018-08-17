# Provides access to the "Image" function from the "PIL" Package
from PIL import Image

def invert(im):
    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))

            redInvert = 255 - red
            greenInvert = 255 - green
            blueInvert = 255 - blue
            im.putpixel((x, y), (redInvert, greenInvert, blueInvert))

def invert_block(im):
    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width - width // 2, width):
        for y in range(0,height // 2):
            (red, green, blue) = im.getpixel((x, y))

            redInvert = 255 - red
            greenInvert = 255 - green
            blueInvert = 255 - blue
            im.putpixel((x, y), (redInvert, greenInvert, blueInvert))

######################### FUNCTIONS DEFINED #########################

# Opens the "bear.jpg" file to RAM and creates a pointer to it at "bear"
bear = Image.open("bear.jpg")

# Displays the image that "bear" is pointing to
bear.show()

bear = Image.open("bear.jpg")

invert(bear)
bear.save("bear_inverted.jpg")
bear.show()

bear = Image.open("bear.jpg")
invert_block(bear)
bear.save("bear_invertedBlock.jpg")
bear.show()
