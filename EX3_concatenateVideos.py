from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
clip1 = VideoFileClip("V_1.mp4")
clip2 = VideoFileClip("V_2.mp4")
# .subclip(50,60)
# clip3 = VideoFileClip("myvideo3.mp4")
final_clip = concatenate_videoclips([clip1,clip2])
# final_clip=CompositeVideoClip([clip2,clip1])
final_clip.write_videofile("merged.mp4")