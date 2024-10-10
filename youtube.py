import os
import sys
import subprocess

def download_video(link, title=None, ext='mp4'):
    # Set the filename based on the provided title and extension
    filename = f'{title}.{ext}' if title else None
    
    # If a filename is specified, download the video with the specified filename
    if filename:
        subprocess.run(['yt-dlp', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '-o', filename, link])
    else:
        # If no filename is specified, download the video using the default filename
        subprocess.run(['yt-dlp', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', link])

def download_audio(link, title=None, ext='mp3'):
    # Set the filename based on the provided title and extension
    filename = f'{title}.{ext}' if title else None
    
    # If a filename is specified, download the audio with the specified filename
    if filename:
        subprocess.run(['yt-dlp', '-x', '--audio-format', ext, '-o', filename, link])
    else:
        # If no filename is specified, download the audio using the default filename
        subprocess.run(['yt-dlp', '-x', '--audio-format', ext, link])

if __name__ == '__main__':
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print('Usage: python3 youtube.py -v {link} [-t \'title\'] [-e {extension}] | download Video')
        print('Usage: python3 youtube.py -a {link} [-t \'title\'] [-e {extension}] | download Audio')
        sys.exit(1)

    # Get the option for video or audio
    option = sys.argv[1]
    # Get the YouTube link from the command-line arguments
    link = sys.argv[2]
    title = None
    ext = None

    # Process optional arguments for title and extension
    for i in range(3, len(sys.argv)):
        if sys.argv[i] == '-t' and i + 1 < len(sys.argv):
            title = sys.argv[i + 1]
        elif sys.argv[i] == '-e' and i + 1 < len(sys.argv):
            ext = sys.argv[i + 1]

    # If the extension is not specified, use the default (mp4 for video, mp3 for audio)
    ext = ext if ext else ('mp4' if option == '-v' else 'mp3')

    # Call the appropriate download function based on the option
    if option == '-v':
        download_video(link, title, ext)
    elif option == '-a':
        download_audio(link, title, ext)
    else:
        print('Invalid option. Use -v for video or -a for audio.')
