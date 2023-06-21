import glados_TTS
import voice_recognization
import glados_AI

while True:
    if __name__ == "__main__":
        try:
            glados_TTS.glados_Speaks(glados_AI.glados_Speaks(voice_recognization.voice_recognization()))
        except:
            print("Maximun Failures Reached")
