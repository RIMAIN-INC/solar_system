#Author: Richmond Kwalah Nartey Tettey
#Course: CS1
#Date: 10/31/2024
#Purpose: Solar system Game

from cs1lib import draw_rectangle, set_fill_color, draw_circle, draw_text, set_stroke_color


class Button:
    def __init__(self, name,x,y,width,height, r, g, b):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False
        self.r = r
        self.g = g
        self.b = b
        self.original_color = (r, g, b)  # Store the original color
        self.current_color = (67/255,69/255,75/255)  # Set the current color to original

    def draw(self):

        set_stroke_color(1,1,1)
        draw_text("Select Planets and Press Space bar To Start!", 100,int(500/3))

        # Draw outline of the button
        set_fill_color(*self.current_color)
        draw_rectangle(self.x, self.y, self.width, self.height)

        # Draw the icon of the button as a centered circle
        set_fill_color(self.r,self.g,self.b)
        circle_radius = min(self.width, self.height) // 4  # Scale circle size to fit within button
        circle_x = self.x + self.width // 2
        circle_y = self.y + self.height // 2 - circle_radius // 2  # Center circle vertically in button
        draw_circle(circle_x, circle_y, circle_radius)

        # Draw the text below the circle, centered horizontally within the button
        set_fill_color(0, 0, 0)
        text_width = len(self.name) * 7  # Adjust width based on text length (approximate)
        text_x = self.x + (self.width - text_width) // 2  # Center the text in the button
        text_y = circle_y + circle_radius + 10  # Position text below the circle with padding
        draw_text(self.name, text_x, text_y)



    def toggle_color(self):
        # Toggle color between original and clicked
        if self.clicked:
            self.current_color = self.original_color
        else:
            self.current_color = (67/255,69/255,75/255)
