import subprocess

# We initialize the necessary variables
video = 'BBB.mp4'
N = 12
size = '160x120'


# We cut the video a total of N seconds and save a new version of it
def cut_video(N, input):
    subprocess.call(['ffmpeg', '-ss',  '00:00:00', '-i', str(input), '-c', 'copy', '-t', str(N), 'BBB_cut.mp4'])


# We extract the YUV histogram from the video and create a new version showing it
def yuv_histogram(input):
    subprocess.call(['ffplay', str(input), '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'])


# We resize the input depending on the specified size
def resizing(input, size):
    if size == '720':
        subprocess.call(['ffmpeg', '-i', str(input), '-vf', 'scale=1280:720', 'BBB_resized_720.mp4'])
    elif size == '480':
        subprocess.call(['ffmpeg', '-i', str(input), '-vf', 'scale=720:480', 'BBB_resized_480.mp4'])
    elif size == '360x240':
        subprocess.call(['ffmpeg', '-i', str(input), '-vf', 'scale=360:240', 'BBB_resized_360x480.mp4'])
    elif size == '160x120':
        subprocess.call(['ffmpeg', '-i', str(input), '-vf', 'scale=160:120', 'BBB_resized_160x120.mp4'])


# We convert the stereo audio to mono audio and save it as an audio .wav file
def mono(input):
    subprocess.call(['ffmpeg', '-i', str(input), '-ac', '1', 'BBB_mono.wav'])


# We call all methods
cut_video(N=N, input=video)
yuv_histogram(input=video)
resizing(input=video, size=size)
mono(input=video)