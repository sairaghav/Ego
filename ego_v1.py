import sys,subprocess, time, threading
from ego_api import speaker,listener,reader,browser,process_handler,note_taker,window_switcher,key_presser,volume_controller
from multiprocessing import Process
import google

def get_input():
    speak_data = listener.listen()
    while speak_data == '':
            speaker.speak('Sorry.. Can you say that again??')
            speak_data = listener.listen()
    return speak_data
    

def ego(data):
    global listening
    
    if data in ['hi ego', 'wake up ego', 'hey ego', 'wake up', 'ego']:
        speaker.speak('Hello! I am Ego.. What can I do for you??')
        listening = 1

    if listening == 1:
        if 'what time is it' in data:
            speaker.speak(time.ctime())

        if 'read book' in data:
            global reading
            speaker.speak('Reading...')
            reading = Process(target=reader.read,args=('test.txt',))
            reading.start()

        if 'stop reading' in data:
            reading.terminate()

        if 'search' in data:
            speaker.speak('What do you want me to search for??')
            query = get_input()

            speaker.speak('Searching for '+query)
            threading.Thread(target=browser.browse,args=('https://www.google.com/search?q='+query,)).start()

        if 'play music' in data:
            speaker.speak('Which song do you want me to play??')
            song = get_input() + ' video'

            speaker.speak('Playing '+song)
            threading.Thread(target=browser.browse,args=(google.lucky(song),)).start()
            
        if 'switch window' in data:
            window_switcher.switch_windows(1)

        if 'press' in data:
            key_presser.press_key(data)
            
        if data in ['show desktop','close window','close tab','new tab','restore tab']:
            key_presser.press_key(data)

        if 'take notes' in data:
            note_taker.take_notes()

        if 'volume' in data:
            volume_controller.controller(data)

        if 'close process' in data:
            speaker.speak('Which process do you want me to close??')
            process_to_close = listener.listen()
            procid = process_handler.proc_finder(process_to_close+'.exe')

            if not procid is None:
                process_handler.proc_killer(procid)
                speaker.speak(process_to_close+' is closed')
            else:
                speaker.speak('No process called '+process_to_close+' found')

    if 'go to sleep' in data:
            speaker.speak('Going to sleep..')
            listening = 0
            
    if 'exit' in data:
        speaker.speak('Exiting... Goodbye!')
        sys.exit(0)

if __name__ == '__main__':
    try:
        speaker.speak('Hello! I am Ego.. What can I do for you??')
        listening = 1
        
        while True:
            data = listener.listen()
            ego(data)

    except KeyboardInterrupt:
        sys.exit(0)
