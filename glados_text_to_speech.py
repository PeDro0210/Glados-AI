import pyttsx3
import glados_AI
import voice_recognization
import keyboard


global engine
engine = pyttsx3.init()

def speach_to_text(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.5)
    engine.say(f'<pitch middle="{round(-20*.5+1.50)}">{text}</pitch>')
    engine.runAndWait()

def action_made():
    try:
        print("Press Space to speak")
        while True:
            if keyboard.is_pressed('space'):
                speach_to_text(glados_AI.glados_Speaks(voice_recognization.voice_recognization()))
            else:
                engine.stop()  
    except:
        pass

