import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bacteria Simulation')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Bacteria settings
initial_bacteria = 50
bacteria_size = 5
growth_rate = 0.02  # Probability of duplication per frame
death_rate = 0.01   # Probability of dying per frame

# Bacteria class
class Bacteria:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        self.x = max(0, min(self.x, width))
        self.y = max(0, min(self.y, height))

    def duplicate(self):
        return Bacteria(self.x, self.y)

    def die(self):
        self.alive = False

# Create initial bacteria population
bacteria_population = [Bacteria(random.randint(0, width), random.randint(0, height)) for _ in range(initial_bacteria)]

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    window.fill(WHITE)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update bacteria
    new_bacteria = []
    for bacterium in bacteria_population:
        if bacterium.alive:
            bacterium.move()
            if random.random() < growth_rate:
                new_bacteria.append(bacterium.duplicate())
            if random.random() < death_rate:
                bacterium.die()

    bacteria_population.extend(new_bacteria)
    bacteria_population = [b for b in bacteria_population if b.alive]

    # Draw bacteria
    for bacterium in bacteria_population:
        pygame.draw.circle(window, GREEN, (bacterium.x, bacterium.y), bacteria_size)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()
