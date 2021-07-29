# EzEb
EbSynth is hard to use... Lots of turning videos into image sequences, resizing style images to fit the original frames, renaming the style images to be named like the original frames, and lot's more. I didn't want to do that every single time, so I just automated it. Kind of. And it's still a work in progress. But it does what it's supposed to do. Make using EbSynth easier... That's why it's called EzEb. 

# So what does EzEb do?
EzEb is an automated way of making EbSynth easier to use. It turns videos into image sequences, resizes your style images to fit the original frames, and renames the style images to the name of the original frame, but it's still a work in progress and I'm planning on adding more features.

# Before you first run
- run the requirements.bat file to install the required python libraries for this project
- run the clearDir.py file to get all the folders empty and ready for you to use

# So how can you use this?
Well, it's actually not that hard. Here is a step by step guide:

1. use the clearDir.py file to make sure the folders are empty.
2. put your video into the video folder
3. start EzEb.py
4. use your explorer to go into the frames folder and pick a frame you want to stylize and use as your style image. (Remember the filename. It will tell you what frame number the image is.
5. restyle your image however you want and put the finished thing into the styleOriginal folder.
6. Go back to your Python runtime where you opened EzEb. Make sure you only have one image in the styleOriginal folder and hit enter.
7. Enter the filename I told you to remember. (The frame number that likely has some zeros before it.) and hit Enter again.
8. Do you want to do another one? Delete your style image from the styleOriginal folder (it's already copied into styleCorrect anyway), enter "y", put a new style image in styleOriginal and repeat steps 4. 5. 6. and 7. Maybe also repeat step 8 if you have another style image.
9. Open EbSynth.
10. In your file explorer, go into the main EzEb directory.
11. Drag and drop the frames folder into EbSynth where it says "Video:"
12. Drag and drop the styleCorrect folder into EbSynth where it says "Keyframes:"
13. Drag and drop the render folder into EbSynth where it says "Output:"
14. Click the "Run All" button.
15. Take the frames from the render folder and turn them into a video with your preferred method. (I'm planning on automating that part aswell in the future.)
16. Repeat if you want to make another stylized video.
