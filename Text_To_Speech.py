from gtts import gTTS
import os

x = True
while x:
    mytext = str(input('Enter text here: '))
    language = 'en'
    settings = gTTS(text = mytext, lang = language, slow = False)
    settings.save('audio.mp3')
    os.system('start audio.mp3')