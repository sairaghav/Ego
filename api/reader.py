import listener,speaker,google_search,threading,sys,time,browser


class RunCheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global reading
        global paused

        while reading == 1:
            choice = listener.listen()
            if 'stop' in choice:
                reading = 0
            if 'pause' in choice:
                paused = 1

def read_book(filename):
    global reading
    global paused
    reading = 1
    paused = 0

    position = 0

    with open(filename,'r') as fp:
        RunCheck().start()
        while reading == 1:
            fp.seek(position)
            speaker.speak(fp.readline())
            position = fp.tell()
            
            while paused == 1:
                choice = listener.listen()
                if 'resume' in choice:
                    paused = 0
                if 'stop' in choice:
                    paused = 0
                    reading = 0

def read_news():
    speaker.speak('Is there anything specific that you want to hear about?')
    
    data = listener.listen()

    if ['news','breaking news','top news'] in data or '' in data:
        data = 'news'
        
    if data is '':
        pass
    
    else:   
        for link,headlines in google_search.search_news(data).iteritems():
            speaker.speak(headlines)

            choice = listener.listen()

            if 'next' in choice:
                continue
            elif 'select' in choice:
                browser.browse(link)
                paused = 1
            elif 'stop' in choice:
                break
            elif 'pause' in choice:
                paused = 1

            while paused == 1:
                choice2 = listener.listen()
                if 'resume' in choice2:
                    paused = 0
                if 'stop' in choice2:
                    break
