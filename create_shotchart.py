from matplotlib import image
from matplotlib import pyplot as plt
from PIL import Image

# to read the image stored in the working directory
data = image.imread('COURTMOCKUP.jpg')

# to draw a point on co-ordinate (200,300)
#misses
plt.plot(200, 350, marker='x', ms=5 ,color="red")
plt.plot(193, 608, marker='x', ms=5 ,color="red")
#makes
plt.plot(525, 100, marker='o', ms=5, mec="g", color="white")
plt.imshow(data)
#plt.show()


plt.savefig("ourshotchart.png")
img = Image.open("ourshotchart.png")
img.show()
