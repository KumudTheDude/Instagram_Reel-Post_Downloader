import instaloader
import os
from moviepy.editor import *
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip


# Create an instance of Instaloader class
L = instaloader.Instaloader()
# Get post URL from user input
print(" ")
print(" ")
print(" ")
print("                                          𝕴𝖓𝖘𝖙𝖆𝖌𝖗𝖆𝖒  ")
print(" ")
print("                          Download Videos and Reels with the Audio 📽️🎶")
print(" ")
print(" ")
print(" ")
print(" ")
while True:
    post_url = input("𝙴𝚗𝚝𝚎𝚛 𝚝𝚑𝚎 𝚄𝚁𝙻 𝚘𝚏 𝚝𝚑𝚎 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚅𝚒𝚍𝚎𝚘/𝚁𝚎𝚎𝚕: ")
    print(" ")
    print(" ")
    print(" ")
    if post_url == "exit":
        break
    # Download the post
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])
        L.download_post(post, target='Instagram Video Download')
        print("")
        print("Location: D:\VS Python\Instagram Video Download")
        print("")
    except instaloader.exceptions.InvalidArgumentException:
        print("Invalid Instagram URL. ❌❌❌")
    except instaloader.exceptions.BadResponseException:
        print("Fetching post metadata failed.❌❌❌")
    except Exception as e:
        print(f"An error occurred:❌❌❌ {e}")
    print("                        Download complete!")    

    # Open the download directory in File Explorer
    print("")
    path = r"D:\VS Python\Instagram Video Download"
    folder_path = r"D:\VS Python\Instagram Video Download"
    print(" ")
    print("             🎶🎶 Extracting Audio As a seperate MP3 file 🎶🎶")
    print(" ")
# Get all video files from folder
    video_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith((".mp4", ".mov"))]
  
# Extract audio from each video and save as mp3 file
    for video_path in video_files:
        clip = mp.VideoFileClip(video_path)
        audio_path = os.path.splitext(video_path)[0] + '.mp3'
        clip.audio.write_audiofile(audio_path)

# Open the directory using Windows Explorer         
    os.startfile(path)    
    os.startfile(video_path)
    print("")
    print("")
    print("✌-------------------------------------D O N E-------------------------------------------✌")
    print("")
    print("")
    print("")
    print("")
    print("Next URL")
    print("")
