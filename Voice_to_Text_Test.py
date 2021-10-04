import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)

query = "https://google.com/search?q=" + str(r.recognize_google(audio))
 
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(query)
