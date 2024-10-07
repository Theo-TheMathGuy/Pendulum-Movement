import pygame
from pendulum import Pendulum
from math import atan, sqrt, pi

class Session:
    def __init__(self, g, pendulum_radius=10):
        self.pendulums = []
        self.pendulum_radius = pendulum_radius
        self.g = g

    def update(self, screen, fps):
        for pendulum in self.pendulums:
            pendulum.motion(1/fps, self.g)
            pendulum.display(screen, self.pendulum_radius)

    def add_pendulum(self, pos, center):
        vector = (center[0]-pos[0], center[1]-pos[1])
        if vector[0] == 0:
            angle = pi/2
            angle *= (-1 if vector[1] < 0 else 1)
        else:
            angle = atan(-vector[1]/vector[0]) + (pi/2 if vector[0] < 0 else -pi/2)
        radius = sqrt(vector[0]**2 + vector[1]**2)

        self.pendulums.append(Pendulum(angle, radius, center))
        self.pendulums.sort(key=lambda x: x.cord_length, reverse=True)
    
    def display_center(self, screen, center):
        pygame.draw.circle(screen, (0, 0, 0), center, 5)
    
    def add_preset_1(self, center):
        for k in range(1, 6):
            self.add_pendulum((center[0] + k*25 + 100, center[1]), center)