import yt_dlp
import os

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # This selects the best quality MP4, or best quality of any format if MP4 is not available
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"Title: {info['title']}")
            print(f"Views: {info['view_count']}")
            print(f"Length: {info['duration']} seconds")

            print("Downloading...")
            ydl.download([url])
            print(f"Download completed successfully. Saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("If the error persists, try using a different video URL or checking your internet connection.")

def main():
    while True:
        url = input("Please enter the YouTube video URL (or 'q' to quit): ")
        if url.lower() == 'q':
            break
        
        output_path = r'C:\Users\PC\OneDrive\Documents\PyYoutube\downloaded video'
        download_video(url, output_path)
        print("\n")

if __name__ == "__main__":
    main()