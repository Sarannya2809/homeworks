import pygame

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

color = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == CHANGE_COLOR:
            color = (0, 255, 0) 
        if event.type == pygame.QUIT:
            running = False