import speaker,listener,google_search

def converse():
    conversation = 1
    speaker.speak('What would you like to talk about?')
    
    while conversation == 1:
        data = listener.listen()

        if 'command mode' in data:
            conversation = 0
            speaker.speak('It was nice talking to you. See you soon!')
        
        else:
            answer = google_search.get_summary(data)

            if answer is None and not data is '':
                speaker.speak('Sorry.. I don\'t know anything about that. Can we talk something else?')
            elif answer is None and data is '':
                pass
            else:
                speaker.speak(answer)
