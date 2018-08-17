# My name is Dario Aburto


#Gets the picture of the bear from the library 
from PIL import Image
#Opens the Image of the bear while storing a reference in "bear"
bear = Image.open( "bear.jpg" )

def invert( im ):
    ''' Invert the colors in the input image, im '''
    
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
             # Complete this function by adding your lines of code here.
             
            BearRed = 255 - red
            BearGreen = 255 - green
            BearBlue = 255 - blue
            im.putpixel( (x, y), (BearRed, BearGreen, BearBlue) )
            
        
            # You need to calculate the new pixel values and then to change them
            # in the image using putpixel()





# Pixel size is (600, 800)
bear.size
invert(bear)
bear.show()
bear.save("invertedbear.jpg")
#def invert_block( im )
