try:
    from gtts import gTTS
    from playsound import playsound

    tts = gTTS(text='Good Day Everyone', lang='en')
    tts.save("greeting.mp3")
    playsound(tts)

except ModuleNotFoundError:
    print('Kindly import the Libraries')