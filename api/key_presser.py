import pyautogui

def press_key(data):
        if 'right' in data:
            pyautogui.press('right')
        if 'left' in data:
            pyautogui.press('left')
        if 'up' in data:
            pyautogui.press('up')
        if 'down' in data:
            pyautogui.press('down')
        if 'enter' in data:
            pyautogui.press('enter')
        if 'escape' in data:
            pyautogui.press('esc')
        if 'space' in data:
            pyautogui.press('space')
        if 'tab' in data:
            pyautogui.press('tab')
        if 'shift' in data:
            pyautogui.press('shift')
        if 'control' in data:
            pyautogui.press('ctrl')
        if 'alt' in data:
            pyautogui.press('alt')
        if 'desktop' in data:
            pyautogui.keyDown('win')
            pyautogui.press('d')
        if 'close window' in data:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
        if 'close tab' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')
            pyautogui.keyUp('ctrl')
        if 'new tab' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('t')
            pyautogui.keyUp('ctrl')
        if 'next tab' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('tab')
            pyautogui.keyUp('ctrl')
        if 'previous tab' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('tab')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('ctrl')
        if 'new window' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.press('n')
            pyautogui.keyUp('ctrl')
        if 'restore tab' in data:
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('shift')
            pyautogui.press('t')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('ctrl')
