import navigator,volume_controller,threading

class listener(threading.Thread):
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
