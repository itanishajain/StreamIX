import yt_dlp
import os

os.environ["FFMPEG_BINARY"] = "/opt/homebrew/bin/ffmpeg"

def download_video(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',  # Download both video and audio together
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'concurrent_fragment_downloads': 32,  # Maximize number of simultaneous downloads
            'quiet': True,  # Suppress logs for better speed
            'geo_bypass': True,  # Allow bypass of geographical restrictions
            'merge_output_format': 'mp4',  # Merging video and audio into one file
            'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Specify the correct ffmpeg path
            'hls_prefer_native': True,  # Use native downloader for HLS (streaming)
            'max_downloads': 1,  # Limit concurrent downloads to 1
            'ratelimit': -1,  # Disable rate limit (unrestricted speed)
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
            'socket_timeout': 30,  # Timeout after 30 seconds if stuck
            'retries': 10,  # Retry up to 10 times in case of failure
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video and audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best available audio
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,  # Suppress logs for better speed
            'geo_bypass': True,  # Allow bypass of geographical restrictions
            'ratelimit': -1,  # Disable rate limit (unrestricted speed)
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
            'socket_timeout': 30,  # Timeout after 30 seconds if stuck
            'retries': 10,  # Retry up to 10 times in case of failure
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to YouTube Downloader!")
    print("Select an option:")
    print("1. Download Video")
    print("2. Download Audio")

    choice = input("Enter the number of your choice (1/2): ").strip()

    if choice == '1':
        print("Select the video quality:")
        print("1. 240p")  # Smallest size
        print("2. 360p")
        print("3. 480p")
        print("4. 720p")
        print("5. 1080p")
        
        quality_choice = input("Enter the number of your chosen quality (1-5): ").strip()

        quality_dict = {
            '1': '240',  # Smallest quality
            '2': '360',
            '3': '480',
            '4': '720',
            '5': '1080'
        }

        if quality_choice in quality_dict:
            quality = quality_dict[quality_choice]
        else:
            print("Invalid choice! Defaulting to 720p.")
            quality = '720'

        url = input("Enter YouTube URL: ")
        download_video(url, quality)  # Download both video and audio as part of the video download option
    
    elif choice == '2':
        url = input("Enter YouTube URL: ")
        download_audio(url)
    
    else:
        print("Invalid choice! Please select '1' or '2'.")