import voice_recognization
import glados_AI
from Loading_glados import print_slow

Conversation_engaged=False
while True:
    if __name__ == "__main__":
        try:
            text_said=voice_recognization.voice_recognization()
            if text_said!=None:
                text_said_apart=text_said.lower().split(" ") 

                if "glados," in text_said_apart or "glados" in text_said_apart or "glados." in text_said_apart: #it will only start the conversation if it hears glados
                    Conversation_engaged=True

                if "Good" and "Bye." in text_said_apart and Conversation_engaged==True: #For ending the conversation at the moment
                    glados_AI.handleShutUpMessage(text_said)
                    Conversation_engaged=False

                if "shutdown" in text_said_apart or ("shut" in text_said_apart and "down" in text_said_apart):
                    glados_AI.handleShutUpMessage(text_said)
                    print_slow(f"\033[34mINFO:\033[0m \033[38;5;208mGLaDOS Shutting down.\033[0m\n")
                    break

                if Conversation_engaged: #The boolean flag is on 
                    glados_AI.processMessageGlados(text_said)

        except Exception as e:
            print(f"\033[34m\033[31mERROR:\033[0m \033[38;5;208mMAXIMUN FAILURE\033[0m")    
            print(f"\033[34m\033[31mERROR:\033[0m \033[38;5;208m{e}\033[0m\n")