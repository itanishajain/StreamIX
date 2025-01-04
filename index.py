import os
import yt_dlp

def download_video(url, quality):
    try:
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,  # Avoid downloading playlists
            'merge_output_format': 'mp4',  # Merge video and audio in mp4 format
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
            'noplaylist': True,  # Avoid downloading playlists
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from {url}...")
            ydl.download([url])
        print("Downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
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

if __name__ == "__main__":
    main()
