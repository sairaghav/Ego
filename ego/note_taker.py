import listener,speaker,subprocess,time


def take_notes():
    notes = 1
    note_file = 'note_'+str(time.time()).split('.')[0]+'.txt'

    speaker.speak('Tell me what you want to note down. Please say \'end of note\' to stop the note')

    while notes == 1:
        text = listener.listen()+'\n'
        with open(note_file,'a+') as fp:
            fp.write(text)
        if 'end of note' in text:
            notes = 0
            speaker.speak('Note saved!')
            subprocess.call(['start', 'notepad.exe',note_file],shell=True)
            break
