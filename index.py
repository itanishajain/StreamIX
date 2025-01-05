import yt_dlp

def download_video(url, quality):
    try:
        ydl_opts = {
            'format': f'best[height<={quality}]',  # Download best video + audio format available
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'concurrent_fragment_downloads': 16,  # Increase number of simultaneous downloads
            'quiet': True,  # Suppress logs for better speed
            'hls_prefer_native': True,  # Use native downloader for HLS
            'ffmpeg_location': '/path/to/ffmpeg',  # Specify ffmpeg path (if needed)
            'geo_bypass': True,  # Allow bypass of geographical restrictions
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'geo_bypass': True,  # Allow bypass of geographical restrictions
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to YouTube Downloader!")
    choice = input("Would you like to download video or audio? (video/audio): ").lower()

    if choice == 'video':
        url = input("Enter YouTube URL: ")
        quality = input("Enter the quality (240p, 360p, 480p, 720p, 1080p): ")
        download_video(url, quality)
    
    elif choice == 'audio':
        url = input("Enter YouTube URL: ")
        download_audio(url)
    
    else:
        print("Invalid choice! Please select 'video' or 'audio'.")