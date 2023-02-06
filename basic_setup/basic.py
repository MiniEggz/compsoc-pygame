import pygame

# pygame setup
pygame.init()
screen_size = width, height = (800, 800)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing logic
    screen.fill("green")
    pygame.display.update()
    clock.tick(60)

pygame.quit()