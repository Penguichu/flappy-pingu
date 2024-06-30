import pygame

class Cat:
    def __init__(self, image, sound):
        self.image = image
        self.sound = sound
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.gravity = 0.6
        self.velocity = 0
        self.jump = -10

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.velocity = 0

    def flap(self):
        self.velocity = self.jump
        self.sound.play()
