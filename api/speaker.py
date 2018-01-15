import pyttsx,sys
def speak(text):
    try:
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        print text
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt:
        sys.exit(0)
