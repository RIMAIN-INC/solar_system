#Author:Richmond Kwalah Tettey
#Course: CS1
#Date: 10/29/2024

#System blueprint to create solar system object

from math import sqrt

from cs1lib import cs1_quit

G = 6.67384e-11  #gravitational constant

class System:

    def __init__(self,celestial_bodies):
        self.bodies = celestial_bodies

    #to draw the planets
    def draw(self,center_x,center_y,pixels_per_meter):
        for body in self.bodies:
            body.draw(center_x,center_y,pixels_per_meter)

    #to change velocity for each bodies by acceleration
    def update(self,timestep):
        for i in range(len(self.bodies)):
            (ax,ay) = self.compute_acceleration(i)
            self.bodies[i].update_velocity(ax,ay,timestep)

            self.bodies[i].update_position(timestep)

    def compute_acceleration(self, n):
        ax = 0 #initialize an x component of acceleration
        ay = 0 #initialize an y component of acceleration

        for j in range(len(self.bodies)):
            if j != n:

                dx = self.bodies[j].x - self.bodies[n].x  # x component of distance
                dy = self.bodies[j].y - self.bodies[n].y  # y component of distance

                r_distance = sqrt(dx ** 2 + dy ** 2)  # distance between centers

                # Calculate the gravitational acceleration components
                ax += (G * self.bodies[j].mass / r_distance ** 2) * (dx / r_distance) #acceleration for x
                ay += (G * self.bodies[j].mass/ r_distance ** 2) * (dy / r_distance) #acceleration for y

        return ax, ay