import listener,speaker,google_search

def read_book(filename):
    with open(filename,'r') as fp:
        speaker.speak(fp.read().splitlines())

def read_news():
    speaker.speak('Is there any specific news that you want to hear about? Say BREAKING NEWS if you want to hear the current top news.')
    data = listener.listen()

    if 'breaking news' in data:
        for link,headlines in google_search.search_news().iteritems():
            speaker.speak(headlines)
    elif data is '':
        pass
    else:
        for link,headlines in google_search.search_news(data).iteritems():
            speaker.speak(headlines)
