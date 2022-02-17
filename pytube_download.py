# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:/"  # to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=y9kKqeoobww&t=9s"

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception


yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()