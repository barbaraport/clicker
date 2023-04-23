
import time
from pyautogui import click, moveTo

menu_x = 1305
menu_y = 230

button_x = 1285
button_y =  450 # 300

number_clicks = 3464

time.sleep(6)

for number in range(0, number_clicks):

    moveTo(menu_x, menu_y)
    click(menu_x, menu_y, 1)

    time.sleep(1)

    moveTo(button_x, button_y)
    click(button_x, button_y, 1)

    time.sleep(5)