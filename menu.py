#Author: Richmond Kwalah Nartey Tettey
#Course: CS1
#Date: 10/31/2024
#Purpose: Solar system Game

from button import Button
from body import Body
from cs1lib import draw_text, set_font_size


class Menu:

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.buttons = []
        self.solar = []
        self.win_width = WINDOW_WIDTH
        self.win_height = WINDOW_HEIGHT
        names = ["mercury", "venus", "earth", "mars"]
        color = [[1, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0]]
        button_width = WINDOW_WIDTH // 8  # Set width relative to total window width
        button_height = WINDOW_HEIGHT // 10  # Set height relative to window height

        # Calculate horizontal spacing to center buttons across the canvas
        total_button_area = len(names) * button_width
        total_spacing = WINDOW_WIDTH - total_button_area
        spacing = total_spacing // (len(names) + 1)

        j = 0
        while j < 4:
            x = spacing * (j + 1) + button_width * j
            y = (WINDOW_HEIGHT // 2) - (button_height // 2)  # Center vertically
            add_button = Button(names[j], x, y, button_width, button_height, color[j][0], color[j][1], color[j][2])
            add_button.clicked = False  # Initialize clicked state
            self.buttons.append(add_button)
            j += 1

    def draw(self):
        # Draw all buttons


        for button in self.buttons:
            button.draw()


    def on_click(self, mx, my):
        # Toggle button clicked state if mouse is within button bounds
        for button in self.buttons:
            if button.x <= mx <= button.x + button.width and button.y <= my <= button.y + button.height:
                print(f"first click: {button.clicked}")
                button.clicked = not button.clicked  # Toggle clicked state
                button.toggle_color()                # Change color based on new state

                # Add or remove the planet based on the clicked state
                if button.clicked:
                    print(button.clicked, button.name)
                    self.add_planet(button.name)
                else:
                    print(button.name)
                    self.remove_planet(button.name)

                print(f"after click: {button.clicked}")
                print(f"===========================>")

                break

    def add_planet(self, name):
        # Add planet to the solar system based on the button name
        if name == "mercury":
            mercury = Body("mercury",0.33e24, -57.9e9, 0, 0, 47890, 4, 216 / 255, 87 / 255, 3 / 255)
            self.solar.append(mercury)
        elif name == "venus":
            venus = Body("venus", 4.87e24, -108.2e9, 0, 0, 35040, 6, 0,0,1)
            self.solar.append(venus)
        elif name == "earth":
            earth = Body("earth",5.97e24, -149.6e9, 0, 0, 29790, 7, 0, 1, 1)
            self.solar.append(earth)
        elif name == "mars":
            mars = Body("mars",0.642e24, -227.9e9, 0, 0, 24140, 3, 0, 1, 0)
            self.solar.append(mars)

    def remove_planet(self, this_name):
        # Remove planet from the solar system based on the button name
        for body in self.solar:
            if body.name == this_name:
                self.solar.remove(body)
                print(self.solar)

    def reset_clicks(self):
        # Reset clicked status for all buttons on mouse release
        for button in self.buttons:
            button.clicked = False

    def get_solar(self):
        sun = Body("sun", 1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
        self.solar.append(sun)
        return self.solar