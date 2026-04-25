import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.png")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()