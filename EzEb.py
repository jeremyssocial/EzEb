import os
import cv2
import glob
from PIL import Image
import numpy
import sys


os.chdir(sys.path[0])

vidname = os.listdir("./video")
print(vidname)
os.rename("./video/"+vidname[0],"./video/vid.mp4")

cam = cv2.VideoCapture("./video/vid.mp4")
currentframe = 0
while(True):
    ret,frame = cam.read()

    if ret:
        name = str("./frames/"+str(currentframe).zfill(4)+".jpg")
        print("Frame "+ str(currentframe))
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
cam.release() 
cv2.destroyAllWindows() 


print("nice, now it's time for style.")
more = True
while(more):
    print("if you already have an image in the styleOriginal folder, please remove it.")
    input("then put ONE style picture in the styleOriginal folder and hit enter")
    styleframe = str(input("Which frame is your style picture now? (enter the frame number) "))
    imgname = glob.glob("./styleOriginal/*")
    os.rename(str(imgname[0]),"./styleOriginal/"+styleframe+".jpg")
    imgname = glob.glob("./styleOriginal/*")

    img = Image.open("./frames/"+str(styleframe)+".jpg")
    size = img.size
    im = Image.open(str(imgname[0]))
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("./styleCorrect/"+str(styleframe)+".png", "PNG")
    im.close()

    keepasking = True
    while(keepasking):
        yesORno = str(input("Do you have another one? (y / n)"))
        if yesORno == "y":
            more = True
            keepasking = False
        elif yesORno == "n":
            more = False
            keepasking = False
        else:
            print("either y or n")

#see how many fps the video called "vid.mp4" in the folder "./video" has and save it to a variable called "fps"
vidcap = cv2.VideoCapture("./video/vid.mp4")
fps = vidcap.get(cv2.CAP_PROP_FPS)

#see the height and width of the video called "vid.mp4" in the folder "./video" and save them to the variables "width" and "height"
width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#turn all the frames saved in the folder "./render" into a video called "result.mp4" in the directory "./result". The fps of the video should be the variable "fps" and the width and height should be the variables "width" and "height".
os.system("ffmpeg -r "+str(fps)+" -i ./render/%04d.jpg -i ./video/vid.mp4 -c:v libx264 -pix_fmt yuv420p -r "+str(fps)+" ./result/result.mp4")
