import os
from moviepy.editor import *
from skimage.filters import gaussian
import tkinter as tk
from tkinter import filedialog
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.0.10-Q16\\magick.exe"})

root = tk.Tk()
root.withdraw()

# opens selected video file
file_path = filedialog.askopenfilename()

# video editing
def blur(image):
    """ Returns a blurred (radius=5 pixels) version of the image """
    return gaussian(image.astype(float), sigma=5)


video = VideoFileClip(file_path)
video_resized = video.resize((1080,1920))
video_blurred = video_resized.fl_image( blur )
video_blurred_final = video_blurred.set_fps(5)
video_small = video.resize((1080,640))
video_small_center = video_small.set_pos('center')
video_small_final = video_small_center.set_fps(30)

# file directory and name
dir_name = filedialog.askdirectory()
file_name_extenstion = "/" + input("Enter Clip Name: ")
video_name = dir_name + file_name_extenstion + ".mp4"


final_clip = CompositeVideoClip([video_blurred_final, video_small_final])
final_clip.write_videofile(video_name, codec='libx264', audio_codec='aac' )