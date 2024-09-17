import random
from PIL import Image

#accesing image and finding height and width
img = Image.open(r"C:/Users/rahul/updated_image.png")
pixels = img.load()  # Access pixel data
width, height = img.size



#random pixel selection
sel_pixels = [] #array to store already selected pixels
string = input("Enter input string: ")
strlen = len(string)
key=[]

for k in range (0,strlen):
    
    rand_pixel_height=random.randint(0,height-1)
    rand_pixel_width = random.randint(0,width-1)
    rand_pixel = dict(wt=rand_pixel_width,ht=rand_pixel_height)


    if rand_pixel in sel_pixels:
        k-=1
    else:
        sel_pixels.append(rand_pixel)


#print(sel_pixels)