from pytube import YouTube

url = "https://www.youtube.com/watch?v=2lAe1cqCOXo"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download complete.")
