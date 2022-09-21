import getAudioFromVideo
import YTVideoDownloader
import getTextFromWav
import utils
import os

if __name__ == "__main__":

    toSearch = input("Enter the video name: ")

    videosToDownload = YTVideoDownloader.download(toSearch)
    folderVs = os.listdir("videos")
    for video in folderVs:
        os.rename("videos/" + video, "videos/" + utils.remove_emojis(video))
    getAudioFromVideo.getAudio()
    #print(videosToDownload)

    #getTextFromVideo.getTextFromVideo()
    getTextFromWav.getTranscription()

    
