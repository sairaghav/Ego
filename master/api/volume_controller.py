import pyautogui

def controller(data):
        if 'mute volume' in data:
            pyautogui.press('volumemute')

        if 'increase volume' in data:
            pyautogui.press('volumeup')

        if 'decrease volume' in data:
            pyautogui.press('volumedown')
