import os
import cv2
import glob
from PIL import Image

# Set the current directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Process video
vidname = os.listdir("./video")
if vidname:
    os.rename(f"./video/{vidname[0]}", "./video/vid.mp4")

    cam = cv2.VideoCapture("./video/vid.mp4")
    currentframe = 0
    while True:
        ret, frame = cam.read()
        if ret:
            name = f"./frames/{str(currentframe).zfill(4)}.jpg"
            print(f"Frame {currentframe}")
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

print("Nice, now it's time for style.")

# Style application loop
more = True
while more:
    print("If you already have an image in the styleOriginal folder, please remove it.")
    input("Then put ONE style picture in the styleOriginal folder and hit enter")
    styleframe = input("Which frame is your style picture now? (enter the frame number): ")
    imgname = glob.glob("./styleOriginal/*")
    if imgname:
        os.rename(imgname[0], f"./styleOriginal/{styleframe}.jpg")

    try:
        img = Image.open(f"./frames/{styleframe}.jpg")
        im = Image.open(f"./styleOriginal/{styleframe}.jpg")
        im_resized = im.resize(img.size, Image.ANTIALIAS)
        im_resized.save(f"./styleCorrect/{styleframe}.png", "PNG")
        im.close()
    except IOError as e:
        print(f"Error processing images: {e}")

    while True:
        yes_or_no = input("Do you have another one? (y / n): ").lower()
        if yes_or_no in ["y", "n"]:
            more = yes_or_no == "y"
            break
        else:
            print("Either 'y' or 'n'")

input("Do what you have to do in EbSynth, then return here and press enter")

# Video properties
vidcap = cv2.VideoCapture("./video/vid.mp4")
fps = vidcap.get(cv2.CAP_PROP_FPS)
width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Create final video
if os.path.exists("./render/0001.png"):
    os.system(f"ffmpeg -r {fps} -i ./render/%04d.png -vcodec mpeg4 -y ./result/result.mp4")
elif os.path.exists("./render/0001.jpg"):
    os.system(f"ffmpeg -r {fps} -i ./render/%04d.jpg -vcodec mpeg4 -y ./result/result.mp4")
