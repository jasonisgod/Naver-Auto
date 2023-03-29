import keyboard
import datetime
import time
import pyautogui

print('#jasonisgod')
dt_str = input('YYYY-MM-DD HH:MM:SS.SSS : ')
try:
    dt_target = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')
except:
    print('invalid input')
    exit()
print(dt_target)
print('waiting...')
while True:
    try:
        dt_now = datetime.datetime.now()
        if dt_now > dt_target:
            pyautogui.click()
            print(dt_now)
            print(f'clicked !!!')
            break
    except KeyboardInterrupt:
        break
input('bye')

'''

def fill_form():
    time.sleep(3)
    for i in range(4):
        keyboard.press_and_release('tab')
    for i in range(4):
        keyboard.write('0')
        keyboard.press_and_release('tab')

def loop():
    while True:
        dt = datetime.datetime.now()
        sec = dt.second
        if sec % 10 == 0:
            keyboard.press_and_release('enter')
            print(dt, sec)
            time.sleep(3)
            keyboard.press_and_release('alt+left')
            fill_form()
        pass

if __name__ == '__main__':
    fill_form()
    loop()

import keyboard
import time

N_LINE = 4
DELAY_SLEEP = 3

input_list = []
for i in range(N_LINE):
    input_list.append(input(f'line {i+1}: '))

while True:
    try: 
        if keyboard.is_pressed('delete'):
            for i in range(N_LINE):
                keyboard.write(input_list[i])
                keyboard.press('tab')
            keyboard.press('enter')
    except:
        break

'''