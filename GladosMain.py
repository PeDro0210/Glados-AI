import voice_recognization
import glados_AI
from Loading_glados import print_slow
import os
space_pressed = False
while True:

    # TODO: Refactor the HotWord Stuff
    if __name__ == "__main__":
        try:

            if not space_pressed:
                os.system("cls")
                print("\033[34mINFO:\033[0m \033[38;5;208mPress Space to talk with glados\033[0m ")
                space_pressed = True

            if (voice_recognization.voice_recognization() != None):
                message = voice_recognization.TTSQuery()
                glados_AI.processMessageGlados(message)
                space_pressed = False
            


        except Exception as e:
            print(f"\033[34m\033[31mERROR:\033[0m \033[38;5;208mMAXIMUN FAILURE\033[0m")    
            print(f"\033[34m\033[31mERROR:\033[0m \033[38;5;208m{e}\033[0m\n")

        except KeyboardInterrupt:
            print_slow("\033[34mINFO:\033[0m \033[38;5;208mKeyboard Interrupt Detected\033[0m\n")
            print_slow("\033[34mINFO:\033[0m \033[38;5;208mGLaDOS Shutting down.\033[0m\n")
            exit()