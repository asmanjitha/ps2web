
# @author --- IT16521544 B D K Samaraweera

import cv2
import imutils
import os

def mobileresize(imgname):

    image = cv2.imread('static/Compressed_Images/'+imgname)

    new_image = imutils.resize(image, width=360)

    cv2.imwrite('static/mobile/'+imgname, new_image)



def tabresize(imgname):

    image = cv2.imread('static/Compressed_Images/'+imgname)

    new_image = imutils.resize(image, width=768)

    cv2.imwrite('static/tab/'+imgname, new_image)


def processResizing():

    imagefilelist = os.listdir('static/Images')
    for x in imagefilelist:
        mobileresize(x)
        tabresize(x)

    return "true"



processResizing()