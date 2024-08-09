import os
import whisper
from langdetect import detect
from pytube import YouTube
import subprocess

# Ensure FFmpeg is installed and accessible
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
        print("FFmpeg is installed and accessible.")
    except subprocess.CalledProcessError:
        print("FFmpeg is not accessible. Check your PATH or installation.")
        exit(1)

# Function to open a file
def startfile(fn):
    os.system(f'start {fn}')

# Function to create and open a txt file
def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)
    startfile(filename)

# Ensure FFmpeg path is set
ffmpeg_path = r"C:\ffmpeg\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

# Check if FFmpeg is accessible
check_ffmpeg()

# Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object from the URL
yt = YouTube(url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
output_path = "YoutubeAudios"
os.makedirs(output_path, exist_ok=True)  # Ensure the directory exists
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

# Load the base model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe(os.path.join(output_path, filename))
transcribed_text = result["text"]
print(transcribed_text)

# Detect the language
language = detect(transcribed_text)
print(f"Detected language: {language}")

# Create and open a txt file with the text
create_and_open_txt(transcribed_text, f"output_{language}.txt")
