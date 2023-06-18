import pyttsx3
import glados_AI
import voice_recognization


global engine
engine = pyttsx3.init()

def speach_to_text(text):
    if text != None:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 0.5)
        engine.say(f'<pitch middle="{round(-20*.5+1.50)}">{text}</pitch>')
        engine.runAndWait()

def action_made():
    try:
        speach_to_text(glados_AI.glados_Speaks(voice_recognization.voice_recognization()))
 
    except:
        pass

