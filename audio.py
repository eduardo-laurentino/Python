from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'
#Converte a frase para áudio
sp = gTTS(
    text = 'Estou aprendendo Python',
    lang = language
)
sp.save(audio)
playsound(audio)
