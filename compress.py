# @author --- IT16521544 B D K Samaraweera

import os
from PIL import Image


def compressMe(file,filename):
    filepath = os.path.join(os.getcwd(), file)
    file_extension = os.path.splitext(file)
    picture = Image.open(filepath)

    if file_extension[1] == '.png':
      picture.save("static/Compressed_Images/" + filename, "PNG", optimize=True)

    if file_extension[1] == '.jpeg':
        picture.save("static/Compressed_Images/" + filename, "JPEG", optimize=True, quality=60)

def processCompressing():

    imagefilelist = os.listdir('static/Images')
    print(imagefilelist)

    for x in imagefilelist:
        compressMe('static/Images/'+x,x)

    return "true"



processCompressing()

