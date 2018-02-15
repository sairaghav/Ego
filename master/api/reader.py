from threading import Thread
from time import sleep
from urllib import urlretrieve
from os import getcwd,path,makedirs
import listener,speaker,google_search,browser,pdf_converter,navigator,volume_controller

class RunCheck(Thread):
    def __init__(self):
        Thread.__init__(self)

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
            if choice in ['show desktop','close window','close tab','new tab','restore tab','next tab','previous tab'] or 'switch window' in choice or 'press' in choice or 'scroll' in choice:
                navigator.navigate(choice)
            if 'volume' in choice:
                volume_controller.controller(choice)

def read_book():
    global reading
    global paused
    reading = 1
    paused = 0

    speaker.speak('What book would you like to read?')
    data = listener.listen()
    book_path = getcwd()+'\\Books'
    if path.exists(book_path):
        pass
    else:
        makedirs(book_path)
        
    book_name = book_path+'\\'+data+'.pdf'
    filename = ''
    
    cnt = 0
    while cnt < 5:
        try:
            speaker.speak('Searching for the book.. This may take some time..')
            urlretrieve(google_search.search(data+' ebook filetype:pdf').values()[cnt],book_name)
            filename = pdf_converter.pdf_to_text(book_name)
            speaker.speak('Book obtained. Starting the reader..')
            break
        except:
            cnt += 1
            filename = ''

    if filename == '':
        reading = 0
        speaker.speak('Sorry, I could not find the book. Stopping reader..')
    
    if reading == 1:
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

    for headlines,link in google_search.search_news(data).iteritems():   
        if paused == 0:
            speaker.speak(headlines)
            sleep(5)
        if browse == 1:
            speaker.speak('Pausing news playback to open link')
            paused = 1
            browser.browse(link)
            browse = 0
        while paused == 1:
            pass

    paused = 1
    reading = 0
    speaker.speak('Stopping news playback')
