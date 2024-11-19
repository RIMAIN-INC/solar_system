#Author: Richmond Kwalah Nartey Tettey
#Course: CS1
#Date: 10/31/2024
#Purpose: Solar system Game

from cs1lib import set_fill_color, draw_rectangle, draw_text, set_font_size, set_stroke_color, clear, cs1_quit
from button import Button
from system import System

class Escape:

    def __init__(self,name,x,y,width,height, r, g, b):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.r = r
        self.g = g
        self.b = b
        self.hover_color = (1,1,1)


    def draw_esc(self):
        # Draw outline of the button
        set_fill_color(0,0,0)
        set_stroke_color(0,0,0)
        draw_rectangle(self.x, self.y, self.width, self.height)

        set_font_size(20)
        set_stroke_color(1,1,1)
        draw_text(self.name,int(self.width/len(self.name))-(len(self.name)*3),int(self.height/2))


    def on_click(self,mx,my):
        if self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height:
            cs1_quit()

