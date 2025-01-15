import yt_dlp

def download_video():
    youtube_url = input("Please enter the YouTube video URL: ")
    output_path = input("Please enter the output path for the video (default is current directory): ") or '.'

    ydl_opts = {
        'outtmpl': f"{output_path}/%(title)s.%(ext)s",
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Format selection
        'merge_output_format': 'mp4',  # Output format
        'noplaylist': True,  # Download only the video, not the playlist
        'nooverwrites': True,  # Skip downloading if the file already exists
        'continuedl': True,  # Resume unfinished downloads
        'nocheckcertificate': True,  # Don't check server SSL certificate
        'ratelimit': None,  # No download speed limit
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
download_video()