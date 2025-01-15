# YouTube Video Downloader 📹🎥

This script allows you to download videos from YouTube using the `yt_dlp` library.

## Requirements
- Python 3.x
- `yt_dlp` library
- `ffmpeg` installed on your system

## Installation
1. Download and extract the ZIP file.
2. Navigate to the directory:
    ```sh
    cd path/to/your/directory
    ```

3. Install the required packages:
    ```sh
    pip install yt_dlp
    ```

4. Install `ffmpeg`:
    - **Windows**: Follow the steps on [FFmpeg.org](https://ffmpeg.org/download.html) to download and extract `ffmpeg`, and add it to your system path.
    - **macOS**: Install via Homebrew with `brew install ffmpeg`.
    - **Linux**: Install via package manager (`sudo apt install ffmpeg` for Debian/Ubuntu, `sudo yum install ffmpeg` for CentOS/RHEL).

## Usage
Run the `downloader.py` script and follow the prompts:
```sh
python downloader.py
