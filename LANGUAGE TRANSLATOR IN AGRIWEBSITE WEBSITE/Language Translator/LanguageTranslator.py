import googletrans
import gtts
import speech_recognition
import playsound

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print ("Please Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language="te")
    print (text)

translator = googletrans.Translator()
translation = translator.translate(text, dest="zh-CN")
print (translation.text)
converted_audio = gtts.gTTS(translation.text, lang="te")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")

