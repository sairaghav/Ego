import pyttsx,sys
def speak(text):
    try:
        engine = pyttsx.init()
        engine.setProperty('rate',150)

        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()
    except:
        sys.exit(0)
