import socket
from PIL import Image

def getpixels():
    img = Image.open(r"C:/Users/rahul/updated_image.png")
    pixels = img.load()  # Access pixel data
    width, height = img.size
    total_pixels = width * height
    return width, height, total_pixels

def get_ip_address():
    # Get the IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Get IP address
ip = get_ip_address()

# Convert IP to integer
ip_as_int = int(''.join([bin(int(x)+256)[3:] for x in ip.split('.')]), 2)

# Get image dimensions and total pixels
width, height, total_pixels = getpixels()

#print("IP Address:", ip)
#print("Total pixels:", total_pixels)

key_position_height = ip_as_int % height
key_position_width = ip_as_int % width
#print("Key position:", key_position_height, key_position_width)