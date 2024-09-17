
import keyencryption
import ip
from PIL import Image

img = Image.open("C:/Users/rahul/modified_image.png")
pixels = img.load()  # Access pixel data
mod_sel_pixels = keyencryption.mod_sel_pixels


# !!! WORK AFTER NETWORK SETUP: Extract sender's IP address to calculate KEY POSITION !!! 


key_position_height = ip.key_position_height
key_position_width = ip.key_position_width

sf_RGB = pixels[key_position_width,key_position_height]
sf_binRGB=[]

shift_factor=""

R = bin(sf_RGB[0])[2::].zfill(8)
G = bin(sf_RGB[1])[2::].zfill(8)
B = bin(sf_RGB[2])[2::].zfill(8)

shift_factor=(R[-2::1]+G[-2::1]+B[-3::1]) 
shift_factor=int(shift_factor,2)

#print(mod_sel_pixels)

for index in mod_sel_pixels:
    index["wt"]-=shift_factor
    index["ht"]-=shift_factor

#print(mod_sel_pixels)

message=""

for index in mod_sel_pixels:
    letter=""
    wt=index["wt"]
    ht=index["ht"]
    RGB=pixels[wt,ht]
    R=bin(RGB[0])[2::].zfill(8)
    G=bin(RGB[1])[2::].zfill(8)
    B=bin(RGB[2])[2::].zfill(8)
    letter=R[-2::1]+G[-2::1]+B[-3::1]
    letter = chr(int(letter,2))
    message+=letter
    
print("mesage received:",message)
