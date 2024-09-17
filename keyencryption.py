from PIL import Image 
import ip
import random
import obtain_pixel
import change_image

def binary_list_to_rgb(binary_list):
    
    r = int(binary_list[0], 2)  # Red channel
    g = int(binary_list[1], 2)  # Green channel
    b = int(binary_list[2], 2)  # Blue channel
    return (r, g, b)

img = Image.open(r"C:/Users/rahul/modified_image.png")
pixels =  pixels = img.load()
key_position_height=ip.key_position_height
key_position_width=ip.key_position_width

RGB=pixels[key_position_width,key_position_height]
RGB_bin=[]

shift_factor = random.randint(0,127)
temp=bin(shift_factor)
k_bin = temp[2::].zfill(7)
print("sender side: ",k_bin) 
for values in RGB:
    temp=bin(values)
    RGB_bin.append(temp[2::].zfill(7))
    

R_embed=k_bin[0:2]
G_embed=k_bin[2:4]
B_embed=k_bin[4:7]

RGB_bin[0]=RGB_bin[0][0:len(RGB_bin[0])-2]+R_embed
RGB_bin[1]=RGB_bin[1][0:len(RGB_bin[0])-2]+G_embed
RGB_bin[2]=RGB_bin[2][0:len(RGB_bin[0])-3]+B_embed
#print(RGB_bin)

RGB_dec=binary_list_to_rgb(RGB_bin)
#print(RGB_dec)
pixels[key_position_width,key_position_height] = RGB_dec

mod_sel_pixels = obtain_pixel.sel_pixels

for items in mod_sel_pixels:
    items["wt"]+=shift_factor
    items["ht"]+=shift_factor

modified_image_path = 'C:/Users/rahul/modified_image.png'  # Replace with the path where you want to save the modified image
img.save(modified_image_path)
#print(mod_sel_pixels)