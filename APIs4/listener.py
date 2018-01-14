import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    data = ''

    try:    
        data = str(r.recognize_google(audio)).lower()
        print data
        
    except:
        None

    return data
