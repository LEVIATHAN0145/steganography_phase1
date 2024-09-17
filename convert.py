import obtain_pixel

bin_list=[]
for x in obtain_pixel.string:
    temp=bin(ord(x))
    bin_list.append(((temp[2::]).zfill(7))) #typecasting the binary string to integer and selecting from 3rd index to avoid '0b' 

print(bin_list)


