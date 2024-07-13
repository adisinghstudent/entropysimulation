import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Test')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()

pygame.quit()

# ! [rejected]        main -> main (non-fast-forward)
#  error: failed to push some refs to 'https://github.com/adisinghstudent/entropysimulation.git'
#use when branch is being committed remotely and automatically simulataneously: 
### git push -f -u origin main, ###
# where main is the branch name