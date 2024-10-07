import pygame
from math import sin, cos, atan, pi
from random import randint
class Pendulum:
    def __init__(self, start_angle, cord_length, center, cord_color=(0, 0, 0), pendulum_color=None):
        self.cord_length = round(cord_length)
        self.angle = start_angle
        self.angle_acceleration = 0
        self.angle_velocity = 0
        self.cord_color = cord_color
        if pendulum_color is None:
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            self.pendulum_color = (r, g, b)
        else:
            self.pendulum_color = pendulum_color
        self.center = center
        self.update_pos()
    
    def motion(self, dt, g=9.81):
        self.angle_acceleration = -(g/self.cord_length)*sin(self.angle)
        self.angle_velocity += self.angle_acceleration*dt
        self.angle += self.angle_velocity*dt
        self.update_pos()
    
    def update_pos(self):
        cord_length = self.cord_length
        angle = self.angle
        x, y = cord_length*sin(angle), cord_length*cos(angle)
        self.pos = (round(x), round(y))

    def display(self, screen, radius, center_radius=5):
        center = self.center
        pos = (center[0] + self.pos[0], center[1] + self.pos[1])
        cord_color = self.cord_color
        pendulum_color = self.pendulum_color
        pygame.draw.circle(screen, cord_color, self.center, center_radius)
        pygame.draw.line(screen, cord_color, center, pos, 3)
        pygame.draw.circle(screen, pendulum_color, pos, radius)