# YouTube Transcript Generator

## Overview

This Python script automates the process of downloading audio from a YouTube video, transcribing it using **OpenAI's Whisper model**, detecting the language of the transcription, and saving the transcription to a text file. The text file is automatically opened after creation. The script ensures that **FFmpeg**, a multimedia framework, is installed and accessible for audio processing.

### Key Features:
- **Automated transcription** of YouTube videos.
- **Language detection** of the transcribed text.
- Saves transcription in a text file and opens it automatically.
- Verifies **FFmpeg** installation, ensuring smooth audio processing.

## Modules Used

- **os**: For handling interaction with the operating system, such as managing file paths and running system commands.
- **whisper**: To transcribe audio into text using OpenAI's Whisper model.
- **langdetect**: For detecting the language of the transcribed text.
- **pytube**: For downloading videos and audio streams from YouTube.
- **subprocess**: To execute system-level commands and check if FFmpeg is installed.

## Key Functions

- **`check_ffmpeg()`**: Verifies if FFmpeg is installed and accessible from the system’s PATH. If not, the script exits with an error message.
  
- **`startfile(fn)`**: Opens a file using the default program associated with its file type on the user’s operating system.

- **`create_and_open_txt(text, filename)`**: Creates a text file with the provided content and filename, then opens it.

## Workflow

1. **Set FFmpeg Path**: Adds the FFmpeg binary location to the system PATH environment variable.
  
2. **Check FFmpeg Installation**: The script calls `check_ffmpeg()` to ensure FFmpeg is installed and accessible.
  
3. **YouTube URL Input**: The user is prompted to input a YouTube video URL.
  
4. **Download Audio**: The script uses PyTube to download the audio stream of the YouTube video in MP3 format.
  
5. **Transcribe Audio**: The Whisper model transcribes the downloaded audio into text.
  
6. **Detect Language**: The `langdetect` module identifies the language of the transcribed text.
  
7. **Save and Open Transcription**: The transcribed text is saved into a `.txt` file, named according to the detected language. The file is automatically opened after creation.



## Purpose

This script is ideal for anyone who wants to automate the process of generating transcripts from YouTube videos in different languages. It integrates video downloading, audio processing, and transcription efficiently, making it a powerful tool for content creators, researchers, or anyone needing quick text transcriptions.


---

Let me know if you need any additional details for the README!
