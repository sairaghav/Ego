import psutil

def proc_finder(proc_name):
    for proc in psutil.process_iter():
        if proc.name() == proc_name:
            return proc.pid

def proc_killer(procid):
    for proc in psutil.process_iter():
        if proc.pid == procid:
            proc.kill()
        
