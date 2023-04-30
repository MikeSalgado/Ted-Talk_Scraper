import sys
import os
import speech_recognition as sr

def transcribe_audio(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)

    try:
        transcript = r.recognize_sphinx(audio_data)
        return transcript
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        return None

def transcribe_audio_realtime():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Recording started. Speak now...")

        while True:
            audio_data = r.listen(source, phrase_time_limit=5)

            try:
                transcript = r.recognize_sphinx(audio_data)
                print("Transcription: " + transcript)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        if not os.path.isfile(audio_file):
            print("Error: File not found.")
            sys.exit(1)

        transcript = transcribe_audio(audio_file)

        if transcript is not None:
            print("Transcription: " + transcript)
    else:
        transcribe_audio_realtime()


