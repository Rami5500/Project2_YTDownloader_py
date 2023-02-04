#importing the following library
from pytube import YouTube
from sys import argv

#Will allow us to enter the link in terminal
link = argv[1]

yt = YouTube(link)

print("Title: ", yt.title)
print("views: ", yt.thumbnail_url)

#Fetches the highest
yd = yt.streams.get_highest_resolution()
#created a downloads folder and places it in there
yd.download('Downloads')