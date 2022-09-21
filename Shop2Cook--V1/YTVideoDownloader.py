import getVideosFromYT
import pytube


def download(toSearch):
    videosToDownload = getVideosFromYT.getVideoUrls(str(toSearch))

    for video in videosToDownload:
        try:
            print('Downloading: ' + video['title'])
            pytube.YouTube(video['url']).streams.filter(file_extension="mp4").first().download('videos')
        except:
            print('Error downloading: ' + video['title'])
            continue

    return videosToDownload
