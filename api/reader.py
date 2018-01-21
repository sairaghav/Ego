import listener,speaker,google_search,threading,time,browser,pdf_converter,navigator,volume_controller

class RunCheck(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global reading
        global paused
        global browse

        while reading == 1:
            choice = listener.listen()
            if 'stop' in choice or 'exit' in choice:
                paused = 1
                reading = 0
            if 'pause' in choice or 'wait' in choice:
                paused = 1
            if 'resume' in choice or 'continue' in choice:
                paused = 0
                browse = 0
            if 'select' in choice or 'more' in choice:
                paused = 1
                browse = 1
            if choice in ['show desktop','close window','close tab','new tab','restore tab','next tab','previous tab'] or 'switch window' in choice or 'press' in choice:
                navigator.navigate(choice)
            if 'volume' in choice:
                volume_controller.controller(choice)

def read_book():
    global reading
    global paused
    reading = 1
    paused = 0

    speaker.speak('Provide the full path of the PDF book to be read')
    filename = pdf_converter.pdf_to_text(raw_input('Full File Path: '))

    position = 0

    with open(filename,'r') as fp:
        RunCheck().start()
        while reading == 1:
            if paused == 0:
                fp.seek(position)
                speaker.speak(fp.readline())
                position = fp.tell()

        paused = 1
        reading = 0

        speaker.speak('Stopping the reader')

def read_news():
    global reading
    global paused
    global browse
    reading = 1
    paused = 0
    browse = 0
    
    speaker.speak('Is there anything specific that you want to hear about?')
    
    data = listener.listen()
    
    if 'nothing' in data:
        data = ''
    
    RunCheck().start()

    for headlines,link in google_search.search(data).iteritems():   
        if paused == 0:
            speaker.speak(headlines)
            time.sleep(5)
            if browse == 1:
                speaker.speak('Pausing news playback to open link')
                browser.browse(link)
                browse = 0
            
        while reading == 1 and paused == 1:
            if browse == 1:
                browser.browse(link)
                browse = 0
            else:
                pass

    paused = 1
    reading = 0
    speaker.speak('Stopping news playback')
