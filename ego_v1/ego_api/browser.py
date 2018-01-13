import subprocess

def browse(link):
    subprocess.Popen(['start', 'chrome.exe', link], shell=True)
