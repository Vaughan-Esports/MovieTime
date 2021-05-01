from moviepy.editor import *


async def tiktok_blur(file_path):
    # opens selected video file
    video = VideoFileClip(file_path)

    # render video
    video.write_videofile('temp/output.mp4',
                          ffmpeg_params=['-lavfi', '[0:v]scale=256/81*iw:256/81*ih,boxblur=luma_radius=min(h\,w)/40:luma_power=3:chroma_radius=min(cw\,ch)/40:chroma_power=1[bg];[bg][0:v]overlay=(W-w)/2:(H-h)/2,setsar=1,crop=w=iw*81/256'])