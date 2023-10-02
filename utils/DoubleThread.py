from Loading_glados import print_slow
import glados_TTS as speak
from concurrent.futures import ThreadPoolExecutor


def MultiThreading(Prompt):
    executor = ThreadPoolExecutor(max_workers=2)
    voice_future = executor.submit(speak.glados_Speaks, Prompt)
    printy_future = executor.submit(print_slow, (f"\033[34mINFO:\033[0m \033[38;5;208m{Prompt} \033[0m\n"))
    voice=voice_future.result()
    printy=printy_future.result() #Same stuff about the variables