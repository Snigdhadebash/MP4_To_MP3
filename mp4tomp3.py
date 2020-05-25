import moviepy.editor as mp

clip = mp.VideoFileClip(r'C:\Users\CISPL- SNIHDHADEB\Desktop\mp4tomp3\youtube.mp4')
clip.audio.write_audiofile(r'C:\Users\CISPL- SNIHDHADEB\Desktop\mp4tomp3\youtubeaudio.mp3')
print("Completed...")