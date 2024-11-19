#Author:Richmond Kwalah Tettey
#Course: CS1
#Date: 10/29/2024
#Body blueprint to instantiate solar body object


from cs1lib import *

class Body:
    def __init__(self,name,mass, x, y, x_velocity, y_velocity,radius, r,g,b): # x and y  are the  locations and v_x and v_y are the velocity of ball
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.v_x = x_velocity
        self.v_y = y_velocity
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    #method to draw the object with a specific color
    def draw(self,center_x,center_y,pixels_per_meter):
        set_fill_color(self.r,self.g,self.b)
        draw_circle(center_x + self.x * pixels_per_meter,center_y + self.y * pixels_per_meter,self.radius)

    #method to change position of object by its velocity
    def update_position(self,timestep):
        self.x += self.v_x * timestep
        self.y += self.v_y * timestep

    #method to change velocity of object with acceleration
    def update_velocity(self,ax,ay,timestep):
        self.v_x += ax * timestep
        self.v_y += ay * timestep
