import speaker

def read(filename):
    with open(filename,'r') as fp:
        speaker.speak(fp.read().splitlines())
