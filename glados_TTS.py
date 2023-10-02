import torch
from utils.tools import prepare_text
from scipy.io.wavfile import write
import time
from sys import modules as mod
from Loading_glados import do_all
try:
    import winsound
    import os
    #just windows compatibility
    os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = 'C:\Program Files\eSpeak NG\libespeak-ng.dll'
    os.environ['PHONEMIZER_ESPEAK_PATH'] = 'C:\Program Files\eSpeak NG\espeak-ng.exe'
except ImportError:
    from subprocess import call
import os
from concurrent.futures import ThreadPoolExecutor
import time


if torch.cuda.is_available():
    # Change to 'cuda' when a GPU trained model is available
    device = 'cuda'
else:
    print("Using CPU")
    device = 'cpu'

# Prepare models in RAM
def warmup():    
    # Load models
    glados = torch.jit.load('models\glados.pt', map_location="cpu")
    vocoder = torch.jit.load('models\\vocoder-gpu.pt', map_location=device)

    for i in range(2):
        init = glados.generate_jit(prepare_text(str(i)))
        init_mel = init['mel_post'].to(device)
        init_vo = vocoder(init_mel)

    return glados, vocoder

# Warmup models in a separate thread from the loading screen
executor = ThreadPoolExecutor(max_workers=2)
warmpup_Future = executor.submit(warmup)
Loading_glados_Future = executor.submit(do_all)
warmpuload=warmpup_Future.result()
Loading_gladosload=Loading_glados_Future.result()

# loads the models from the thread
glados = warmpuload[0]
vocoder = warmpuload[1]


def glados_Speaks(text):

    # Tokenize, clean and phonemize input text
    x = prepare_text(text).to('cpu') #For the moment, we only support CPU

    with torch.no_grad():

        # Generate generic TTS-output
        old_time = time.time()
        tts_output = glados.generate_jit(x)

        # Use HiFiGAN as vocoder to make output sound like GLaDOS
        old_time = time.time()
        mel = tts_output['mel_post'].to(device)
        audio = vocoder(mel)
        
        # Normalize audio to fit in wav-file
        audio = audio.squeeze()
        audio = audio * 32768.0
        audio = audio.cpu().numpy().astype('int16')
        output_file = ('Audios\output.wav')
        
        # Write audio file to disk
        # 22,05 kHz sample rate
        write(output_file, 22050, audio)

        # Play audio file
        if 'winsound' in mod:
            winsound.PlaySound(output_file, winsound.SND_FILENAME)
        else:
            try:
                call(["aplay", "Audios\output.wav"])
            except FileNotFoundError:
                call(["pw-play", "Audios\output.wav"])
