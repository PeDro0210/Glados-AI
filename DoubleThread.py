from Loading_glados import print_slow
from gladosTTS.glados import tts_runner
from concurrent.futures import ThreadPoolExecutor

glados = tts_runner(False, True)

def MultiThreading(Prompt):
        executor = ThreadPoolExecutor(max_workers=2)
        voice_future = executor.submit(glados.speak, Prompt, True)
        printy_future = executor.submit(print_slow, (f"\033[34mINFO:\033[0m \033[38;5;208m{Prompt} \033[0m\n"))
        voice=voice_future.result()
        printy=printy_future.result() 
