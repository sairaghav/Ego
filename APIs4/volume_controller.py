import pyautogui,speaker

def controller(data):
        if 'mute volume' in data:
            speaker.speak('Muting Volume')
            pyautogui.press('volumemute')

        if 'increase volume' in data:
            speaker.speak('Increasing Volume')
            pyautogui.press('volumeup')

        if 'decrease volume' in data:
            speaker.speak('Decreasing Volume')
            pyautogui.press('volumedown')
