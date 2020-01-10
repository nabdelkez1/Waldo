# Noureldin Abdel Kerim

# Making the pictures
searchImage = makePicture(pickAFile())
template = makePicture(pickAFile())

# Initializing the variables 
w1 = getWidth(template)
w2 = getWidth(searchImage)
h1 = getHeight(template)
h2 = getHeight(searchImage)
x1, y1 = 0, 0

# Compare one function that takes as parameters two images and the coordinates in the search 
# image 
def compareOne(template, searchImage, x1, y1) :
  
  # Initializing the sum
  sum = 0
  
  # Looping through x values in range of width of template
  for x in range(w1) : 
  
  # Looping through y values in range of height of template
    for y in range(h1) :
    
    # Getting values of blue pixels in template and search image since r = g = b 
      blue1 = getBlue(getPixel(searchImage, x1 + x, y1 + y))
      blue2 = getBlue(getPixel(template, x, y))
      
      # Finding SAD and returning it
      sum += abs(blue1 - blue2)
  return sum

# Returns a 2D array containing the computed template match scores for all of the 
# positions in the search image
def compareAll(template, searchImage) :

  # Initializing the matrix 
  matrix = [[0 for i in range(w2)] for j in range(h2)]
  
  # Looping through x values in range of width of search image
  for x in range(w2) : 
  
    # Looping through y values in range of height of search image
    for y in range(h2) :
      
      # Setting pixel coordinates outside boundaries to a large number in order to return
      # correct min values. If left as is, the value will be 0, therefore giving the wrong
      # min value  
      if x >= w2 - w1 or y >= h2 - h1 :
        matrix[y][x] = 1000000
      
      # If within the boundaries, recall the compareOne function
      else :
        matrix[y][x] = compareOne(template, searchImage, x, y)
  return matrix 

# Returns the coordinates of the position in array matrix where the value is a minimum 
def find2Dmin(matrix) :
  # Setting the min to a large arbitrary number 
  min = 1000000
  
  # Looping through x values in range of width of search image
  for x in range(w2) :
  
  # Looping through y values in range of height of search image
    for y in range(h2) : 
    
    # If the position in array matrix is less than the minimum set it to the min variable 
    # and return the position 
      if matrix[y][x] < min : 
        min = matrix[y][x]
        x1 = x
        y1 = y
  return x1, y1

# The function puts a retangle on the searchImage at (x1, y1)
def displayMatch(searchImage, x1, y1, w1, h1, color) :
  addRect(searchImage, x1, y1, w1, h1 + 10, color)

# Grayscaling both pictures to make r = g = b
def grayscale(picture) :

  # Looping through all pixels in the picture 
  for pixel in getPixels(picture) :
    # Get RGB values
    r, g, b = getRed(pixel), getGreen(pixel), getBlue(pixel)
    
    # Find average of RGB and set it to the color
    intensity = (r + g + b)/3
    setColor(pixel, makeColor(intensity, intensity, intensity))

# Recalling all previous functions and displaying the search image with Waldo encapsulated by 
# a rectangle  
def findWaldo(targetJPG, searchJPG) :
  grayscale(searchImage)
  grayscale(template)
  matrix = compareAll(template, searchImage)
  x, y = find2Dmin(matrix)
  displayMatch(searchImage, x, y, w1, h1, blue)
  show(searchImage)