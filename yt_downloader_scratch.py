from pytube import YouTube
import os

"""
IMPORTANT:

GO TO lib > pytube > cypher.py
CHANGE THIS REGEX TO THE ONE MENTIONED BELOW

# legacy

# r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*',
# r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',

# replace by:

r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
"""

def download(link):

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    try:
        print("Downloading ....")
        
        url = YouTube(link)

        video = url.streams.get_highest_resolution()
        
        video.download("downloads")

        print("Donwloaded successfully")

    except Exception as e :
        print(e)

if __name__ == "__main__":

    link = "https://www.youtube.com/watch?v=LK7-_dgAVQE"
    download(link)
