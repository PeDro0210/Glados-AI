import glados_TTS
import glados_AI
import voice_recognization


def speach_to_text(text):
    glados_TTS.glados_Speaks(text)

def action_made():
    try:
        speach_to_text(glados_AI.glados_Speaks(voice_recognization.voice_recognization()))
    except:
        pass
