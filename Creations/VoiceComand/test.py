from gtts import gTTS
from playsound import playsound


language = 'pt-br'


audio = gTTS(
    text='Eu sou horrivel pra isso',
    lang=language,
)

audio.save('audio.mp3')
playsound('audio.mp3')