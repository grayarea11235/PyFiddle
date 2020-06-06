import praw



reddit = praw.Reddit(client_id='EWjEJYl0A4C7sQ',
                     client_secret='UYJATekK9TDAdAQ1an1bJ14SfGM',
                     password='Dribble1',
                     user_agent='testscript by /u/st11235',
                     username='st11235')

print(reddit.user.me())
