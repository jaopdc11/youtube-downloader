
# YouTube Downloader Script

## Overview
This script allows you to download videos or audio from YouTube using `yt-dlp`. You can specify the title and the file format for the downloaded file. It supports both video and audio downloads.

## Requirements

- **Python**: Make sure Python 3.x is installed.
- **yt-dlp**: Install it via pip:
  ```bash
  pip install yt-dlp
  ```
- **ffmpeg**: Necessary for audio extraction. Install it with:
  ```bash
  sudo apt install ffmpeg
  ```

## Usage

Run the script with the following command format:

### Download Video:
```bash
python3 youtube.py -v {link} [-t "title"] [-e {extension}]
```

### Download Audio:
```bash
python3 youtube.py -a {link} [-t "title"] [-e {extension}]
```

- `-v`: Indicates a video download.
- `-a`: Indicates an audio download.
- `-t`: (Optional) Sets the file name for the output.
- `-e`: (Optional) Sets the file extension (default is `mp4` for video and `mp3` for audio).

### Example

1. **Download Video**:
   ```bash
   python3 youtube.py -v https://www.youtube.com/watch?v=dQw4w9WgXcQ -t "MyVideo" -e mp4
   ```

2. **Download Audio**:
   ```bash
   python3 youtube.py -a https://www.youtube.com/watch?v=dQw4w9WgXcQ -t "MyAudio" -e mp3
   ```

## Default Behavior

- If no title is provided, the file will use the default title from the YouTube video.
- If no extension is provided, `mp4` is used for videos and `mp3` for audio.

## Requirements Recap

Make sure the following are installed before running the script:
- Python 3.x
- yt-dlp (installed via pip)
- ffmpeg (for audio downloads)

## License

This script is free to use and distribute.
