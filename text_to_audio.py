from gtts import gTTS
from playsound import playsound
# import pdb

# pdb.set_trace()
def play_it(path):
    playsound(path)

def convert_to(text):
    audio = gTTS(text)
    audio.save('my_audio.mp3')
    play_it('my_audio.mp3')

text = input('enter string you want to be read : ')
try:
    convert_to(text)
except:
    print('check your enternet connection')
    
