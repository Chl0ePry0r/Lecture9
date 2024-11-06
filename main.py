#ImageFilters.py
from PIL import Image
from PIL import ImageFilter

def createRainbow():
  img = Image.new( 'RGB', (250,250), "black") # create a new black image
  pixels = img.load() # create the pixel map

  for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
      pixels[i,j] = (i, j, 100) # set the colour accordingly

  img.save("rainbow.png", 'png')

def swapGreenBlue(img):
  #this function should swap the blue and green pixel values
  pixels = img.load() #Pixels is the pixel map, a 2-dimensional list of pixel data
  width, height = img.size
  for x in range(width):
    for y in range(height):
      red,green,blue, alpha = pixels[x,y]
      pixels[x,y] = (red, blue, green, alpha)

  img.save("swapGB.png", 'png')

def darken(img, amount):
  #this function should darken the r,g,b values by the amount
  #remember to not go below zero on any of the colors
  pixels = img.load() #Pixels is the pixel map, a 2-dimensional list of pixel data
  width, height = img.size
  for x in range(width):
    for y in range(height):
      red,green,blue, alpha = pixels[x,y]
      red = max(red- amount,0)
      green = max(green - amount, 0)
      blue = max(blue - amount, 0)

      pixels[x,y] = (red, green, blue, alpha)
  img.save("darkImg.png", 'png')

def bwFilter(img):
  pixels = img.load() #Pixels is the pixel map, a 2-dimensional list of pixel data
  width, height = img.size
  for x in range(width):
    for y in range(height):
      red,green,blue, alpha = pixels[x,y]
      ave = (red + green + blue)//3
      pixels[x,y] = (ave, ave, ave, alpha)

  img.save("bwImg.png", 'png')

def redPop(img):
  pixels = img.load() #Pixels is the pixel map, a 2-dimensional list of pixel data
  width, height = img.size
  for x in range(width):
    for y in range(height):
      red,green,blue, alpha = pixels[x,y]
      ave = (red + green + blue)//3
      if red > 150 and blue <150 and green <150:
          pixels[x,y] = (red, green, blue, alpha)
      else:
        pixels[x,y] = (ave, ave, ave, alpha)
  
  img.save("redPop.png", 'png')

def main():
  #Open an image
  myImg = Image.open('durango.png')


  #createRainbow()
  #bwFilter(myImg)
  #swapGreenBlue(myImg)
  #darken(myImg, 100)
  redPop(myImg)

  # Buit-in Filters
  im1 = myImg.filter(ImageFilter.BLUR)
  im1.save("blurImg.png", 'png')

if __name__ == '__main__':
  main()
