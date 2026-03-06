"""
YouTube Downloader (yt-dlp wrapper)
created and published by atrx07 
Usage: python yt_downloader.py <video_url> [audio_only]
Requires: yt-dlp (pip install yt-dlp)
Example: python yt_downloader.py https://youtu.be/abcd1234 audio
"""
import sys, subprocess, shlex, os

def download(url, audio_only=False):
    if audio_only:
        cmd = f"yt-dlp -x --audio-format mp3 {shlex.quote(url)}"
    else:
        cmd = f"yt-dlp {shlex.quote(url)}"
    print("Running:", cmd)
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python yt_downloader.py <video_url> [audio]")
    else:
        url = sys.argv[1]
        audio = len(sys.argv) > 2 and sys.argv[2].lower().startswith("a")
        download(url, audio)
