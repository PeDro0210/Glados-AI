import time
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
comencing=[r"Initializing.",r"GLaDOS Activating, Pleas Wait...",r"GLaDos is ready."]

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)  

def print_info_slow(comencing,info,Logo):
    print_slow("\033[38;5;208m" + Logo + "\033[0m")
    print("\n")
    for i in comencing:
        print(f"\033[34m{info}\033[0m \033[38;5;208m{i}\033[0m")
        time.sleep(2)

def do_all():
    print_info_slow(comencing,Info,Logo)


