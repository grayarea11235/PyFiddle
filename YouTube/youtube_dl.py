import pytube


url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

youtube = pytube.YouTube(url)

video = youtube.streams.first()
# or
video = youtube.streams.get_highest_resolution()

video.download() # In Same Folder
# or
video.download('/Downloads') # In Other Folder

video.title # Title
video.video_id # Id
video.age_restricted # Age

video.streams.all()
stream = video.streams.all()
for i in stream:
    print(i)

