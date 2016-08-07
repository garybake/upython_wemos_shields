import ssd1306
from machine import I2C, Pin
from time import sleep_ms

# Simple demo of bouncing a ball around the oled screen

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(64, 48, i2c)
display.fill(0)

width = 60
height = 48

# initial position for our circle
circle_x = 20
circle_y = 20
# how much to move the circle on each frame
move_x = 1
move_y = -1

def draw_circle(display, x0, y0, radius):
    # Draw a cirle or radius at x0, y0
    x = radius
    y = 0
    err = 0

    while x >= y:
        display.pixel(x0 + x, y0 + y, 1)
        display.pixel(x0 + y, y0 + x, 1)
        display.pixel(x0 - y, y0 + x, 1)
        display.pixel(x0 - x, y0 + y, 1)
        display.pixel(x0 - x, y0 - y, 1)
        display.pixel(x0 - y, y0 - x, 1)
        display.pixel(x0 + y, y0 - x, 1)
        display.pixel(x0 + x, y0 - y, 1)

        y += 1
        err += 1 + 2*y
        if 2*(err-x) + 1 > 0:
            x -= 1
            err += 1 - 2*x

while True:
    # Move the circle
    circle_x = circle_x + move_x
    circle_y = circle_y + move_y

    # Handle what happens when we hit the edge
    if circle_x > width:
        circle_x = width
        move_x = -move_x
    elif circle_x < 0:
        circle_x = 0
        move_x = -move_x

    if circle_y > height:
        circle_y = height
        move_y = -move_y
    elif circle_y < 0:
        circle_y = 0
        move_y = -move_y

    # Redraw the circle
    display.fill(0)
    draw_circle(display, circle_x, circle_y, 2)
    display.show()
