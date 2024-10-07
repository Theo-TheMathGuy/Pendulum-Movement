import pygame
from session import Session

pygame.init()

## World Constants ##
G = 9.81
FPS = 180

## Display Constants ##
WIDTH, HEIGHT = 900, 600
center_color = (0, 0, 255)
pendulum_radius = 12

## Actual Code ##
G *= 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pendulum simulation")

running = True
clock = pygame.time.Clock()

session = Session(G, pendulum_radius)

center = None
last_pos = None

while running:
    screen.fill((255, 255, 255))
    session.update(screen, FPS)
    if center is not None:
        session.display_center(screen, center)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            last_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if center is None:
                center = event.pos
            else:
                session.add_pendulum(event.pos, center)
                center = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                center = None
            if event.key == pygame.K_1:
                session.add_preset_1(last_pos)
    clock.tick(FPS)