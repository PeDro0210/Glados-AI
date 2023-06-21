from speech_recognition import Recognizer,Microphone,WaitTimeoutError
from dotenv import load_dotenv
import openai
from API_KEYS_FOR_FRIENDS import Open_AI_API


Open_AI_KEY= Open_AI_API
recognizer = Recognizer()
model="whisper-1"



def voice_recognization():
    try:
        with Microphone() as Users_microphone:
            print(f"\033[34mINFO:\033[0m \033[38;5;208mGlados is listening\033[0m")
            Users_audio = recognizer.listen(Users_microphone, timeout=5)
            print(f"\033[34mINFO:\033[0m \033[38;5;208mGlados done listening\033[0m")
            with open("Audios/microphone-results.wav", "wb") as f:
                f.write(Users_audio.get_wav_data())

        openai.api_key = Open_AI_KEY

        with open("Audios/microphone-results.wav", "rb") as audio_file:
            glados_response = openai.Audio.transcribe(file=audio_file, model=model)

            if glados_response['text']=="" or glados_response['text']==" " or glados_response['text']==None:
                pass
            else:                
                return glados_response['text']
        
    except WaitTimeoutError:
        pass
