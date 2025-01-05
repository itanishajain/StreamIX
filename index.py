import yt_dlp
import os

os.environ["FFMPEG_BINARY"] = "/opt/homebrew/bin/ffmpeg"

def download_video(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',  # Download both video and audio together
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'concurrent_fragment_downloads': 16,  # Increase number of simultaneous downloads
            'quiet': True,  # Suppress logs for better speed
            'geo_bypass': True,  # Allow bypass of geographical restrictions
            'merge_output_format': 'mp4',  # Merging video and audio into one file
            'ffmpeg_location': '/opt/homebrew/bin/ffmpeg',  # Specify the correct ffmpeg path
            'hls_prefer_native': True,  # Use native downloader for HLS (streaming)
            'max_downloads': 1,  # Limit concurrent downloads to 1
            'ratelimit': -1,  # Disable rate limit (unrestricted speed)
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading both video and audio from {url}...")
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
            'quiet': True,
            'geo_bypass': True,  # Allow bypass of geographical restrictions
            'ratelimit': -1,  # Disable rate limit (unrestricted speed)
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def download_both(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',  # Download both video and audio together
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'concurrent_fragment_downloads': 16,  # Increase number of simultaneous downloads
            'quiet': True,  # Suppress logs for better speed
            'geo_bypass': True,  # Allow bypass of geographical restrictions
            'merge_output_format': 'mp4',  # Merging video and audio into one file
            'ffmpeg_location': '/path/to/ffmpeg',  # Specify ffmpeg path if needed
            'hls_prefer_native': True,  # Use native downloader for HLS (streaming)
            'max_downloads': 1,  # Limit concurrent downloads to 1
            'ratelimit': -1,  # Disable rate limit (unrestricted speed)
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading both video and audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to YouTube Downloader!")
    print("Select an option:")
    print("1. Download Video")
    print("2. Download Audio")
    print("3. Download Both Video and Audio")

    choice = input("Enter the number of your choice (1/2/3): ").strip()

    if choice == '1' or choice == '3':
        print("Select the video quality:")
        print("1. 240p")
        print("2. 360p")
        print("3. 480p")
        print("4. 720p")
        print("5. 1080p")
        
        quality_choice = input("Enter the number of your chosen quality (1-5): ").strip()

        quality_dict = {
            '1': '240',
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

        if choice == '1':
            download_video(url, quality)
        elif choice == '3':
            download_both(url, quality)
    
    elif choice == '2':
        url = input("Enter YouTube URL: ")
        download_audio(url)
    
    else:
        print("Invalid choice! Please select '1', '2', or '3'.")