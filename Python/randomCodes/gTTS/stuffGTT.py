from gtts import gTTS

blabla = ("Spoken text")

tts = gTTS(text=blabla, lang='en')

tts.save("C:/test.mp3")
