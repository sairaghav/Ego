import pyautogui,listener,platform

def switch_windows(switcher):
    if platform.release() == '10':
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        pyautogui.keyUp('win')
        while switcher == 1:
            data = listener.listen()
            if 'right' in data:
                pyautogui.press('right')
                switcher = 1
            if 'left' in data:
                pyautogui.press('left')
                switcher = 1
            if 'up' in data:
                pyautogui.press('up')
                switcher = 1
            if 'down' in data:
                pyautogui.press('down')
                switcher = 1
            if 'select' in data:
                pyautogui.press('return')
                break
            if 'close' in data:
                pyautogui.press('enter')
                pyautogui.keyDown('alt')
                pyautogui.press('f4')
                pyautogui.keyUp('alt')
                break
            if 'escape' in data:
                pyautogui.press('esc')
                break

    if platform.release() == '7':
        pyautogui.keyDown('win')
        pyautogui.press('tab')
        while switcher == 1:
            data = listener.listen()
            if 'next' in data:
                pyautogui.press('tab')
                switcher = 1
            if 'previous' in data:
                pyautogui.keyDown('shift')
                pyautogui.press('tab')
                pyautogui.keyUp('shift')
                switcher = 1
            if 'select' in data:
                pyautogui.keyUp('win')
                break


