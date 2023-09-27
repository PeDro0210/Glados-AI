import voice_recognization
import glados_AI

Conversation_engaged=False
while True:
    if __name__ == "__main__":
        try:
            text_said=voice_recognization.voice_recognization()
            if text_said!=None:
                text_said_apart=text_said.lower().split(" ")    

                if "temperature." in text_said_apart:
                    glados_AI.glados_Speaks("temperature.")
                else:
                    if "glados," in text_said_apart or "glados" in text_said_apart or "glados." in text_said_apart:
                        Conversation_engaged=True

                    if "shut" and "up." in text_said_apart and Conversation_engaged==True:
                        glados_AI.glados_Speaks("shut up.")
                        Conversation_engaged=False

                    if Conversation_engaged:
                        glados_AI.glados_Speaks(text_said)
        except:
            print(f"\033[34m\033[31mERROR:\033[0m \033[38;5;208mMAXIMUN FAILURE\033[0m")    