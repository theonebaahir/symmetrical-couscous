import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change on Boundary")

clock = pygame.time.Clock()

# Color options
colors = [pygame.Color('red'), pygame.Color('green'), pygame.Color('blue'), pygame.Color('yellow'), pygame.Color('magenta')]

# Sprite class
class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, pos, velocity):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = random.choice(colors)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=pos)
        self.velocity = pygame.Vector2(velocity)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        hit = False

        # Bounce off boundaries and change color
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity.x *= -1
            hit = True

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.velocity.y *= -1
            hit = True

        if hit:
            self.change_color()

    def change_color(self):
        new_color = random.choice([c for c in colors if c != self.color])
        self.color = new_color
        self.image.fill(self.color)

# Create two sprites with different starting positions and velocities
sprite1 = MovingSprite((100, 100), (3, 2))
sprite2 = MovingSprite((400, 300), (-2, -3))

# Sprite group
sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw
    sprites.update()

    screen.fill((30, 30, 30))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


