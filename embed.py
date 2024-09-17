import obtain_pixel
import convert

string = obtain_pixel.string
bin_list = convert.bin_list
#print(bin_list)

pixels = obtain_pixel.pixels
sel_pixels=obtain_pixel.sel_pixels
bin_RGB=[]
for i in range(0,len(sel_pixels)):
    ht=sel_pixels[i]["ht"]
    wt=sel_pixels[i]["wt"]
    RGB=pixels[wt,ht]
    RGB_BIN=[]    
    for values in RGB:
        temp=bin(values)
        RGB_BIN.append(temp[2::].zfill(8)) # caution: do later research on bit padding (7/8)
    bin_RGB.append(RGB_BIN)
#print("RGB list before embedding: ",bin_RGB)
RGB_count=0
for bin_letter in bin_list:
    R_embed=bin_letter[0:2]
    G_embed=bin_letter[2:4]
    B_embed=bin_letter[4:7]

    bin_RGB[RGB_count][0]=bin_RGB[RGB_count][0][0:len(bin_RGB[RGB_count][0])-2]+R_embed
    bin_RGB[RGB_count][1]=bin_RGB[RGB_count][1][0:len(bin_RGB[RGB_count][0])-2]+G_embed
    bin_RGB[RGB_count][2]=bin_RGB[RGB_count][2][0:len(bin_RGB[RGB_count][0])-3]+B_embed
    RGB_count+=1

#print("RGB list after embedding: ",bin_RGB)    