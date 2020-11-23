#! python3

from pytube import YouTube
from moviepy.editor import *
import os
import eyed3


dir = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
with open(dir+"/to_download.txt") as file: 
    for lien in file:
        #print(lien)
        #input("Press any key to continue...")
        #get title
        title = YouTube(lien).streams.filter(progressive=True, file_extension='mp4').first().title
        print("Found : "+title)
        #input("Press any key to continue...")
        #actual dl
        YouTube(lien).streams.filter(progressive=True, file_extension='mp4').first().download(dir+"/sons")
        print("------> "+title+" downloaded")
        #input("Press any key to continue...")
        
        #convert to .mp3
        videoclip = VideoFileClip(dir+"/sons/"+title+".mp4")
        audioclip = videoclip.audio
        audioclip.write_audiofile(dir+"/sons/"+title+".mp3")
        print("------> "+title+" converted to .mp3\n")
        #input("Press any key to continue...")
        audioclip.close()
        videoclip.close()
        os.remove(dir+"/sons/"+title+".mp4")        
        
        #edit tags
        mp3 = eyed3.load(dir+"/sons/"+title+".mp3")
        try:
            artist, song = title.split(' - ')[0], title.split(' - ')[1]
            #print("song: "+song)
            #print("artist: "+artist)
            #input("Press any key to continue...")
        except:
            song, artist = title, ''
        mp3.tag.title = song
        mp3.tag.artist = artist
        mp3.tag.save()