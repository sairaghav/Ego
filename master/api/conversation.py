import speaker,listener,google_search

def get_response(data):
    answer = google_search.get_summary(data)

    if data == '':
        pass
    elif (answer is None or answer == ''):
        speaker.speak('Sorry.. I don\'t know about that. Ask me something else')
    else:
        speaker.speak(answer)

def converse(data='$'):
    if data == '$':
        conversation = 1
        speaker.speak('What would you like to talk about?')
        
        while conversation == 1:
            data = listener.listen()

            if 'end conversation mode' in data:
                conversation = 0
                speaker.speak('It was nice talking to you. See you soon!')
            
            else:
                get_response(data)
    else:
        get_response(data)
