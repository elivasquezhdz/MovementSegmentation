# MovementSegmentation
Generates image segmentation of frame images in a specified folder and saves them to another.

Dependencies:

Open Cv
Imutils

Usage:

python imgseg.py start_index end_index sourcefolder destintation_folder

It will take the frame images from the source folder starting by start_index to end_index,it will detect movement, and save the movement segments to the destination folder
