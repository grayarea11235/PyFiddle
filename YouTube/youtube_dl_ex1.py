import pytube


url = 'https://www.youtube.com/watch?v=kakU6kQDmU4'
# url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'

youtube = pytube.YouTube(url)
# video = youtube.streams.first()
video = youtube.streams.get_highest_resolution()
video.download()
