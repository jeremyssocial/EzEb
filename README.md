# EzEb

EzEb simplifies the process of using EbSynth, a tool that can be complex due to its requirements of converting videos to image sequences, resizing style images, renaming style images to match frame names, and more. This automation, albeit a work in progress, effectively eases the use of EbSynth - hence the name EzEb.

## What Does EzEb Do?

EzEb automates several processes to make EbSynth more user-friendly:
- Converts videos into image sequences
- Resizes style images to match original frames
- Renames style images to correspond with frame names
- Converts frames from the 'render' folder back into a video

Please note that EzEb is still evolving, with more features planned for future releases.

## Before Your First Run

Ensure the following preparations are made:
- Run `requirements.bat` to install necessary Python libraries.
- Ensure ffmpeg is installed on your system.
- Use `clearDir.py` to prepare the directories for use.

## Using EzEb: A Step-by-Step Guide

1. Run `clearDir.py` to clear the directories.
2. Place your video in the 'video' folder.
3. Launch `EzEb.py`.
4. In the 'frames' folder, select a frame to style. Remember its file name as it indicates the frame number.
5. Style this frame as desired and place the result in the 'styleOriginal' folder.
6. Return to `EzEb.py`, ensure only one image is in 'styleOriginal', and press Enter.
7. Input the remembered frame number and press Enter.
8. If styling another frame, remove the current style image from 'styleOriginal', input 'y', add a new style image, and repeat steps 4-7.
9. Launch EbSynth.
10. In EzEb's main directory, use the file explorer to:
    - Drag and drop the 'frames' folder into EbSynth at "Video:"
    - Drag and drop 'styleCorrect' into EbSynth at "Keyframes:"
    - Drag and drop the 'render' folder into EbSynth at "Output:"
11. Click "Run All" in EbSynth.
12. Once processing is complete, return to EzEb and press Enter to convert frames in 'render' into a video in the 'result' folder.
13. Repeat these steps for additional stylized videos.
