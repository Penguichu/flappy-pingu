import pygame

def show_menu(screen, font):
    screen.fill((0, 0, 0))
    title_text = font.render("Flappy Cat", True, (255, 255, 255))
    start_text = font.render("Press SPACE to Start", True, (255, 255, 255))
    screen.blit(title_text, (100, 200))
    screen.blit(start_text, (50, 300))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

