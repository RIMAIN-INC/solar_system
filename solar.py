#Author: Richmond Kwalah Nartey Tettey
#Course: CS1
#Date: 10/31/2024
#Purpose: Solar system Game


# Imports and initial setup
from cs1lib import *
from system import System
from body import Body
from menu import Menu
from escape import Escape

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7 / 1e10

FRAMERATE = 30
TIMESTEP = 1 / FRAMERATE

is_space_press = False
is_onclick = False
esc_pressed = False
my_mouse_mx = 0
my_mouse_my = 0

new_menu = Menu(WINDOW_WIDTH, WINDOW_HEIGHT)
escape_button = Escape("exit",10,0,int(WINDOW_WIDTH/10),int(WINDOW_HEIGHT/10),0,0,1)
def main():
    global is_space_press, is_onclick, esc_pressed
    set_clear_color(0, 0, 0)  # black background
    clear()

    if is_space_press:
        solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
        escape_button.draw_esc()
        solar.update(TIMESTEP * TIME_SCALE)
    else:
        set_fill_color(int(30/255), int(31/255), int(33/255))
        draw_rectangle(0, 0, int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
        new_menu.draw()

        if is_onclick:
            new_menu.on_click(my_mouse_mx, my_mouse_my)
            is_onclick = False  # Reset after single toggle
            print("method accessed")


solar = System(new_menu.get_solar())

def my_keypressed(value):
    global is_space_press
    if value == " ":
        is_space_press = True
        print("space_pressed")

def my_keyreleased(value):
    global is_space_press
    # if value == " ":
    #     is_space_press = False
    # return

def my_mouse_press(mx, my):
    global my_mouse_my, my_mouse_mx, is_onclick,esc_pressed
    my_mouse_mx = mx
    my_mouse_my = my
    is_onclick = True
    esc_pressed = escape_button.on_click(mx, my)

def my_mouse_release(mx, my):
    global is_onclick, esc_pressed
    is_onclick = False
    esc_pressed = False

start_graphics(main, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
               key_press=my_keypressed, key_release=my_keyreleased,
               mouse_press=my_mouse_press, mouse_release=my_mouse_release)
