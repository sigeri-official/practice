import pyautogui
import os
import time

screen_size = pyautogui.size()

def sum_time(*args):
    return_time = [0, 0, 0, 0, 0, 0]
    for time_stamp in args:
        time_stamp = time_stamp.split(':')
        for i in range(len(time_stamp)):
            try:
                return_time[-i-1] += int(time_stamp[-i-1])
            except:
                pass

    return_time[-2] = return_time[-1] // 60 + return_time[-2] % 60
    return_time[-1] = return_time[-1] % 60
    return_time[-3] = return_time[-1] // 60 + return_time[-2] // 60 + return_time[-3] % 24
    return ':'.join(map(str, return_time[-3:]))

def bold(text):
    return f'\033[1m{text}\033[0m'

class Que():
    def __init__(self):
        self.que = []
        self.help = lambda: print('\n'.join([
            f'1. add: Add a new task to the Que. ({bold("function")}, timestamp (H:M:S, e.g. 10:50:5))',
            '2. start: Start the Que, it will run your tasks in time.'
        ]))

    def add(self, func=lambda: None, time_=''):
        if type(func[0]) == type([]):
            for task in func:
                if task[1][0] == 't':
                    self.que.append([task[0], sum_time(task[1][1:], ':'.join(map(str, time.localtime()[:6])))])
                else:
                    self.que.append(task)
        else:
            self.que.append([lambda: func(), time_])

    def start(self):
        while self.que:
            for i, task in enumerate(self.que):
                if task[1] == ':'.join(map(str, time.localtime()[6-len(task[1].split(':')):6])) or task[1] == '':
                    task[0]()
                    self.que.pop(i)
            time.sleep(0.9)


class Mouse():
    def __init__(self):
        self.help = lambda: print('\n'.join([
            f'1. move: Put your cursor to an exact point. ({bold("X")}, {bold("Y")}, duration (s))',
            f'2. moveBy: Move your cursor relatively by x pixel. ({bold("X")}, {bold("Y")}, duration (s))',
            f'3. drag: Drag your cursor to a pixel. ({bold("X")}, {bold("Y")}, duration (s))',
            '4. click: Click with your cursor. (button (L/R/M), X, Y, count)',
            '5. scroll: Scroll! (unit)',
            '6. get_position: Get your cursors current position. (wait)'
        ]))

    def move(self, x, y, duration=0):
        pyautogui.moveTo(x, y, duration)

    def moveBy(self, x, y, duration=0):
        pyautogui.moveTo(pyautogui.position()[0] + x, pyautogui.position()[1] + y, duration)
    
    def drag(self, x, y, duration=0):
        pyautogui.dragTo(x, y, duration)
    
    def click(self, button='L', x=None, y=None, count=1):
        if x is not None or y is not None:
            pyautogui.move(pyautogui.position()[0] if x is None else x, pyautogui.position()[1] if y is None else y)

        for _ in range(count):
            if button.upper() in ['L', 'LEFT']:
                pyautogui.click(button='left')
            elif button.upper() in ['R', 'RIGHT']:
                pyautogui.click(button='right')
            elif button.upper() in ['M', 'MIDDLE']:
                pyautogui.click(button='middle')

    def scroll(self, unit=3):
        pyautogui.scroll(unit)
    
    def get_position(self, wait=1):
        time.sleep(wait)
        print(f'X = {pyautogui.position()[0]} | Y = {pyautogui.position()[1]}')
        return pyautogui.position()[0], pyautogui.position()[1]
    

class Keyboard():
    def __init__(self):
        self.help = lambda: print('\n'.join([
            f'1. write: Write a text with your keyboard. ({bold("text")}, delay)',
            f'2. key: Press, release or hold a key on your keyboard. ({bold("key")}, action, duration (s))'
        ]))

    def write(self, text, delay=0.01):
        pyautogui.write(text, delay)

    def key(self, key, action='P', duration=1):
        if action.upper() in ['P', 'PRESS']:
            pyautogui.keyDown(str(key))
        elif action.upper() in ['R', 'RELEASE']:
            pyautogui.keyUp(str(key))
        elif action.upper() in ['H', 'HOLD']:
            pyautogui.keyDown(str(key))
            time.sleep(duration)
            pyautogui.keyUp(str(key))


class Screen():
    def __init__(self):
        self.help = lambda: print('\n'.join([
            f'1. message: Open up a message window. ({bold("text")}, title, button)',
            f'2. confirm: Open up a confirmation window. ({bold("text")}, title, buttons)',
            f'3. input: Open up a text input window. ({bold("text")}, title)',
            '4. shot (screen.shot): Take a screenshot of your screen. (X1, Y1, X2, Y2, name)',
            f"5. pixel: Get an exact pixel's color. ({bold('X')}, {bold('Y')})",
            f"6. pixel_match: Check a pixel's color. ({bold('X')}, {bold('Y')}, {bold('RGB')}, tolerance)"
        ]))

    def message(self, text='No text added!', title='Action Builder', button='Ok'):
        pyautogui.alert(text=text, title=title, button=button)
    
    def confirm(self, text='No text added!', title='Action Builder', buttons=['Ok', 'Cancel']):
        return pyautogui.confirm(text=text, title=title, buttons=buttons) == buttons[0]
    
    def input(self, text='No text added!', title='Action Builder'):
        return pyautogui.prompt(text=text, title=title)
    
    def shot(self, x1=0, y1=0, x2=screen_size[0], y2=screen_size[1], name='_'.join(map(str, time.localtime()[:6]))+'.png'):
        pyautogui.screenshot(name, region=(x1, y1, x2, y2))

    def pixel(self, x, y):
        return pyautogui.pixel(x, y)
    
    def pixel_match(self, x, y, RGB, tolerance=0):
        return pyautogui.pixelMatchesColor(x, y, tuple(*RGB), tolerance)


class File():
    def __init__(self):
        self.help = lambda: print('\n'.join([
            f'1. start: Open/start/run a file. ({bold("path")})',
            f'2. delete: Delete a file. ({bold("path")}, sure)',
            f'3. create: Create a new file or dir. ({bold("name")})'
        ]))

    def start(self, path):
        os.startfile(path)
    
    def delete(self, path, sure=False):
        display_path = path.split('/')[-1]
        if not sure:
            sure = Screen().confirm(f"Do you want to delete '{display_path}'?\n({path})", 'Deletion confirm')
        if sure:
            os.remove(path)

    def create(self, name='new'):
        if len(name.split('.')) != 1:
            with open(name, 'w'):
                pass
        else:
            os.mkdir(name)
                

mouse = Mouse()
keyboard = Keyboard()
file = File()
screen = Screen()
que = Que()

presets = {  # You can create your own presets like these. You can create countdowns with 't', e.g. 't10' for a 10 sec countdown or set a fixed point of time.
    'a2s':[[lambda: mouse.move(100, 200), 't5'], [mouse.click, 't7'], [lambda: keyboard.write('Test123'), 't9']]
}


