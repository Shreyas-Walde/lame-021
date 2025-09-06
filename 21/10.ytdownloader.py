from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import time

def download_video(url, save_path):
    try:
        print(f"Attempting to download: {url}")
        print(f"Save path: {save_path}")

        # Create YouTube object with more options
        yt = YouTube(
            url,
            use_oauth=False,
            allow_oauth_cache=True
        )
        
        # Add a small delay to let metadata load
        time.sleep(1)
        
        print(f"Title: {yt.title}")

        streams = yt.streams.filter(progressive=True, file_extension="mp4") # settings type
        highest_res_stream = streams.get_highest_resolution() # for high res v
        highest_res_stream.download(output_path=save_path)
        print("YT vid downloaded successfully!")

    except Exception as e:
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {str(e)}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":  # directly runs this file
    root = tk.Tk()   # initialize the window
    root.withdraw()  # hide window

    video_url = input("Enter url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("started ....")
        download_video(video_url, save_dir)
    else:
        print("select folder plzz")