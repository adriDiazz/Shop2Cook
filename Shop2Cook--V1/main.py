import downloadVideos
import getTextFromVideo



if __name__ == "__main__":

    toSearch = input("Enter the video name: ")

    videosToDownload = downloadVideos.downloadVideos(toSearch)
    print(videosToDownload)

    getTextFromVideo.getTextFromVideo()

    
