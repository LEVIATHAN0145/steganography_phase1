from PIL import Image
import embed
import ip


sel_pixels=embed.sel_pixels
bin_RGB=embed.bin_RGB

def binary_list_to_rgb(binary_list):
    
    r = int(binary_list[0], 2)  # Red channel
    g = int(binary_list[1], 2)  # Green channel
    b = int(binary_list[2], 2)  # Blue channel
    return (r, g, b)

RGB_dec=[]
for item in bin_RGB:
    RGB_dec.append(binary_list_to_rgb(item))

#print(RGB_dec)
"""
# Example data
pixel_updates = [
    {'x': 10, 'y': 20},
    {'x': 15, 'y': 25},
    {'x': 30, 'y': 35}
]


rgb_values = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255)   # Blue
]
"""

# Open an existing image
image_path = 'C:/Users/rahul/updated_image.png'  # Replace with the path to your image
image = Image.open(image_path)

# Ensure the image is in RGB mode (if not, convert it)
if image.mode != 'RGB':
    image = image.convert('RGB')

# Access the pixel data
pixels = image.load()

# Apply the RGB values to the specified pixels
for update, rgb in zip(sel_pixels, RGB_dec):
    x, y = update['wt'], update['ht']
    if 0 <= x < image.width and 0 <= y < image.height:  # Check if the coordinates are within the image boundaries
        pixels[x, y] = rgb

# Save or display the modified image
modified_image_path = 'C:/Users/rahul/modified_image.png'  # Replace with the path where you want to save the modified image
image.save(modified_image_path)
#image.show()
