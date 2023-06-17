import speech_recognition as sr
from dotenv import load_dotenv
import os
import openai



load_dotenv()
Open_AI_KEY= os.getenv('Open_AI_API')
recognizer = sr.Recognizer()
model="whisper-1"



def voice_recognization():
    try:
        with sr.Microphone() as Users_microphone:
            print("Recognizing...")
            Users_audio = recognizer.listen(Users_microphone,timeout=5)
            print("Recognizing done! Saving...")
            with open("microphone-results.wav", "wb") as f:
                f.write(Users_audio.get_wav_data())

        openai.api_key = Open_AI_KEY

        with open("microphone-results.wav", "rb") as audio_file:
            glados_response = openai.Audio.transcribe(file=audio_file, model=model)
            return glados_response['text']
    except:
        return "Error 504ValveInteractive: I'm not in position to answear you that rigth now, inferior human, try again, someday"

open ("requirements.txt","w").write("openai\nspeechrecognition\npython-dotenv\nrequests\npydub\npyaudio\npyttsx3\nrequests\nkeyboard\ndatetime\n")