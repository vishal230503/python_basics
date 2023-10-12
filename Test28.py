from pytube import YouTube

# URL of the YouTube video you want to download
video_url = 'https://www.youtube.com/watch?v=VIDEO_ID_HERE'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream (usually stream with both video and audio)
video_stream = yt.streams.get_highest_resolution()

# Provide a file path to save the video
save_path = '/path/to/save/video.mp4'

# Download the video
video_stream.download(output_path=save_path)

print("Video download completed!")
