import moviepy.editor as mp # pip install moviepy 
video=mp.VideoFileClip('Video.MP4')
logo=(mp.ImageClip('YBTV.png')
        .set_duration(video.duration)
        .resize(height=50)
        .margin(right=20, top=20, opacity=0)
        .set_pos('right', 'top'))
final=mp.CompositeVideoClip([video, logo])
final.subclip(0).write_videofile('VideoAndLogo.MP4')