import torch
from utils.tools import prepare_text
from scipy.io.wavfile import write
import time
from sys import modules as mod
import Loading_glados
try:
    import winsound
    import os
    os.environ['PHONEMIZER_ESPEAK_LIBRARY'] = 'C:\Program Files\eSpeak NG\libespeak-ng.dll'
    os.environ['PHONEMIZER_ESPEAK_PATH'] = 'C:\Program Files\eSpeak NG\espeak-ng.exe'
except ImportError:
    from subprocess import call
import os


if torch.cuda.is_available():
    Loading_glados.print_slow(f"\033[34mINFO:\033[0m \033[38;5;208mGPU name: {torch.cuda.get_device_name(0)}\n")
    Loading_glados.print_slow(f"\033[34mINFO:\033[0m \033[38;5;208mSorry, for the moment we don't support GPU.\033[0m\n")
    # Change to 'cuda' when a GPU trained model is available
    device = 'cpu'
else:
    print("Using CPU")
    device = 'cpu'


# TODO: Wait for the developer to get a GPU trained model for glados
# Load models
glados = torch.jit.load('src\models\glados.pt', map_location=device)
vocoder = torch.jit.load('src\\models\\vocoder-gpu.pt', map_location=device)

# Prepare models in RAM
for i in range(2):
    init = glados.generate_jit(prepare_text(str(i)))
    init_mel = init['mel_post'].to(device)
    init_vo = vocoder(init_mel)

Loading_glados.do_all()
def glados_Speaks(text):

    # Tokenize, clean and phonemize input text
    x = prepare_text(text).to(device)

    with torch.no_grad():

        # Generate generic TTS-output
        old_time = time.time()
        tts_output = glados.generate_jit(x)
        # print("Forward Tacotron took " + str((time.time() - old_time) * 1000) + "ms")

        # Use HiFiGAN as vocoder to make output sound like GLaDOS
        old_time = time.time()
        mel = tts_output['mel_post'].to(device)
        audio = vocoder(mel)
        # print("HiFiGAN took " + str((time.time() - old_time) * 1000) + "ms")
        
        # Normalize audio to fit in wav-file
        audio = audio.squeeze()
        audio = audio * 32768.0
        audio = audio.cpu().numpy().astype('int16')
        output_file = ('src\Audios\output.wav')
        
        # Write audio file to disk
        # 22,05 kHz sample rate
        write(output_file, 22050, audio)

        # Play audio file
        if 'winsound' in mod:
            winsound.PlaySound(output_file, winsound.SND_FILENAME)
        else:
            try:
                call(["aplay", "src\Audios\output.wav"])
            except FileNotFoundError:
                call(["pw-play", "src\Audios\output.wav"])
