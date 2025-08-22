import pyautogui
import time
import random

TIMER = 10
MOVE_AMOUNT = 10  # Move 10 pixels
# Get resolution
screen_width, screen_height = pyautogui.size()

print(f'Mouse Jiggle v1.0\nscreen_width: {screen_width}, screen_height: {screen_height}')

while True:
    # Actual mouse position
    x_start, y_start = pyautogui.position()

    # Wait
    time.sleep(TIMER)

    # Mouse position after 10 s
    x_end, y_end = pyautogui.position()

    print(f'Position startX:{x_start}, startY{y_start}, endX:{x_end}, endY:{y_end}')
    # Mouse is not moving, move it
    if x_start == x_end and y_start == y_end:
        print("Moving")

        new_x = max(10, min(screen_width - MOVE_AMOUNT, x_end + random.randint(-MOVE_AMOUNT, MOVE_AMOUNT)))
        new_y = max(10, min(screen_height - MOVE_AMOUNT, y_end + random.randint(-MOVE_AMOUNT, MOVE_AMOUNT)))
        pyautogui.moveTo(new_x, new_y, duration=0.5)