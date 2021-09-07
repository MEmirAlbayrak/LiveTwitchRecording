import moviepy.editor as mpe

def combine_audio(vidname, audname, outname, fps=60): 
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

combine_audio("output.avi", "output.mp3", "merge_output.mp4")