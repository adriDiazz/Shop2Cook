import moviepy.editor as mp
import speech_recognition as sr
import os


def getTextFromVideo():
    folderLs = os.listdir("videos")
    print(folderLs)


    for title in folderLs:
        titleWithOUtExt = title.split(".")[0]
        # video = mp.VideoFileClip(f"videos/{titleWithOUtExt}.mp4")
        # audio = video.audio

        # audio.write_audiofile(f"audios/{titleWithOUtExt}.wav")

        r = sr.Recognizer()

        with sr.AudioFile(f"audios/{titleWithOUtExt}.wav") as source:
            audio = r.record(source, duration=100)

        try:
            text = r.recognize_google(audio, language="es-ES")
            try:
                with open(f"textos/{titleWithOUtExt}.txt", "w") as f:
                    f.write(text)
            except:
                print("Error writing text")
        except:
            print("Error")


if __name__ == "__main__":
    getTextFromVideo()
