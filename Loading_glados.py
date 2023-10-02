import time
import winsound
Logo=r"""             .,-:;//;:=,
          . :H@@@MM@M/H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M/@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@/@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X/@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%/$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM/H;,-+HMM@M+ /MMMX=
       =%@M@M/@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H/MMMMMMM@= =,
               =++%%%%+/:-."""



Info=r"INFO:"
comencing=[r"Initializing.",r"GLaDOS Activating, Please Wait...",r"GLaDos is ready."]

def print_slow(text, speed=0.01):
    #it will send the text letter by letter, with a delay of 0.01 seconds
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)  

def print_info_slow(comencing,info,Logo):
    #it will print the logo and the info, and then it will print the comencing list
    print_slow("\033[38;5;208m" + Logo + "\033[0m",speed=0.01)
    print("\n")
    for i in comencing:
        print_slow(f"\033[34m{info}\033[0m \033[38;5;208m{i}\033[0m\n")
        time.sleep(2)

def do_all():
    #it will print the logo and the info, and then it will print the comencing list
    print_info_slow(comencing,Info,Logo)
    winsound.PlaySound("Audios\glados_startup.wav", winsound.SND_ASYNC)


