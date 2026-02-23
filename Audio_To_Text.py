import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as elemento:
    print('Escuchando:')
    audio=r.listen(elemento)
    try:
        texto=r.recognize_google(audio,language='es-ES')
        print('Resultado: {}'.format(texto))
        with open('audio.wab','wb') as fichero:
            fichero.write(audio.get_wav_data())
    except:
        print('Intente de nuevo.')
        