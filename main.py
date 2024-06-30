import pygame
from cat import Cat
import menu
import score

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Pingu")

clock = pygame.time.Clock()

high_score = score.load_high_score()

cat_image = pygame.image.load('images/pingu.png')
cat_sound_click = pygame.mixer.Sound('sounds/jump_sound.wav')
cat_sound_lose = pygame.mixer.Sound('sounds/lose_sound.wav')

background_image = pygame.image.load('images/background.png')

font = pygame.font.Font(None, 36)

def main():
    global high_score
    cat = Cat(cat_image, cat_sound_click)
    running = True
    game_over = False
    score_value = 0

    menu.show_menu(screen, font)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        game_over = False
                        cat = Cat(cat_image, cat_sound_click)
                        score_value = 0
                    else:
                        cat.flap()

        if not game_over:
            cat.update()

        screen.blit(background_image, (0, 0))
        screen.blit(cat.image, cat.rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
