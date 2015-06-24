import wave
import math
morse_dict = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
        'F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-',
        'L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
        'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--',
        'X':'-..-','Y':'-.--','Z':'--..',' ':' '}

DIT_LEN = 30
DAH_LEN = DIT_LEN*3
BIG_LEN = DIT_LEN*7

to_encode = raw_input().upper()

symbols = []

for letter in to_encode:
    symbols += [morse_dict[letter]]

frames_per_dot = 0.17143*250000.0
freq           = 1020
frame_rate     = 250000.0
period         = frame_rate / float(freq)
omega          = math.pi*2/period
scale          = 16384
N   = int(frames_per_dot)
dit = map(lambda x: scale*math.sin(x*omega),range(  N))
dah = map(lambda x: scale*math.sin(x*omega),range(3*N))
dit_space = [0]*len(dit)
dah_space = [0]*len(dah)

output = []
sample_dict = {'.':dit,'-':dah,' ':[]}


for grp in symbols:
    for symbol in grp:
        output += sample_dict[symbol] + dit_space
    output += dah_space

signal = ''
for amp in output:
    signal += wave.struct.pack('h',amp)

wav_file = wave.open(to_encode+'.wav','w')
wav_file.setframerate(250000) #250kHz
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.writeframes(signal)
wav_file.close()

