import instaloader
import subprocess
import time

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
        print("ocation: D:\VS Python\Instagram Video Download")
        print("")
        print("                        Download complete!")
    except instaloader.exceptions.InvalidArgumentException:
        print("Invalid Instagram URL. ❌❌❌")
    except instaloader.exceptions.BadResponseException:
        print("Fetching post metadata failed.❌❌❌")
    except Exception as e:
        print(f"An error occurred:❌❌❌ {e}")

        # Open the download directory in File Explorer
    print("")
    path = r"D:\VS Python\Instagram Video Download"
    subprocess.Popen(f'explorer "{path}"')    
    print("")
    print("✌-----------------------------------------------------------------------------------✌")
    print("")
    print("              Download Videos and Reels with the Audio from 𝕴𝖓𝖘𝖙𝖆𝖌𝖗𝖆𝖒  📽️🎶 ")
    print("")
    print("")

