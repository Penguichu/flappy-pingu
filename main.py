import pgzrun
import random

WIDTH = 400
HEIGHT = 600

cat = Actor("cat")
cat.pos = (75, HEIGHT // 2)
gravity = 0.6
velocity = 0
jump = -10
pipes = []
score = 0
game_over = False

def draw():
    screen.blit("background", (0, 0))
    cat.draw()
    for pipe in pipes:
        pipe.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

    if game_over:
        screen.draw.text("Game Over!", color="white", midtop=(WIDTH // 2, HEIGHT // 2))

def update():
    global velocity, game_over, score

    if not game_over:
        velocity += gravity
        cat.y += velocity

        for pipe in pipes:
            pipe.x -= 2
            if cat.colliderect(pipe):
                game_over = True

            if pipe.right < 0:
                pipes.remove(pipe)
                score += 1

        if cat.y > HEIGHT or cat.y < 0:
            game_over = True

        if keyboard.space and not game_over:
            velocity = jump

        if len(pipes) < 5:
            create_pipe()

def create_pipe():
    top_pipe = Actor("pipe-green", pos=(WIDTH, random.randint(200, HEIGHT - 200)))
    bottom_pipe = Actor("pipe-green", pos=(WIDTH, top_pipe.y + 800))
    bottom_pipe.angle = 180
    pipes.append(top_pipe)
    pipes.append(bottom_pipe)

pgzrun.go()
