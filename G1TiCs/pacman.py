import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Pac-Man variables
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_radius = 20
pacman_speed = 5
direction = "RIGHT"
mouth_angle = 0
mouth_opening = True

# Pellet variables
pellet_radius = 5
pellets = [(100, 100), (200, 150), (300, 200), (400, 250), (500, 300)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
        direction = "UP"
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
        direction = "DOWN"
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
        direction = "RIGHT"

    # Screen boundaries
    pacman_x = max(pacman_radius, min(WIDTH - pacman_radius, pacman_x))
    pacman_y = max(pacman_radius, min(HEIGHT - pacman_radius, pacman_y))

    # Mouth animation
    if mouth_opening:
        mouth_angle += 0.1
        if mouth_angle >= math.pi / 4:  # Maximum mouth opening
            mouth_opening = False
    else:
        mouth_angle -= 0.1
        if mouth_angle <= 0:  # Fully closed mouth
            mouth_opening = True

    # Pellet collision
    pellets = [
        pellet for pellet in pellets
        if math.hypot(pacman_x - pellet[0], pacman_y - pellet[1]) > pacman_radius
    ]

    # Drawing
    screen.fill(BLACK)

    # Draw pellets
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, pellet, pellet_radius)

    # Draw Pac-Man
    if direction == "RIGHT":
        pygame.draw.polygon(
            screen, YELLOW,
            [
                (pacman_x, pacman_y),
                (pacman_x + pacman_radius * math.cos(mouth_angle), pacman_y - pacman_radius * math.sin(mouth_angle)),
                (pacman_x + pacman_radius * math.cos(-mouth_angle), pacman_y - pacman_radius * math.sin(-mouth_angle)),
            ]
        )
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    elif direction == "LEFT":
        pygame.draw.polygon(
            screen, YELLOW,
            [
                (pacman_x, pacman_y),
                (pacman_x - pacman_radius * math.cos(mouth_angle), pacman_y - pacman_radius * math.sin(mouth_angle)),
                (pacman_x - pacman_radius * math.cos(-mouth_angle), pacman_y - pacman_radius * math.sin(-mouth_angle)),
            ]
        )
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    elif direction == "UP":
        pygame.draw.polygon(
            screen, YELLOW,
            [
                (pacman_x, pacman_y),
                (pacman_x - pacman_radius * math.sin(mouth_angle), pacman_y - pacman_radius * math.cos(mouth_angle)),
                (pacman_x - pacman_radius * math.sin(-mouth_angle), pacman_y - pacman_radius * math.cos(-mouth_angle)),
            ]
        )
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    elif direction == "DOWN":
        pygame.draw.polygon(
            screen, YELLOW,
            [
                (pacman_x, pacman_y),
                (pacman_x + pacman_radius * math.sin(mouth_angle), pacman_y + pacman_radius * math.cos(mouth_angle)),
                (pacman_x + pacman_radius * math.sin(-mouth_angle), pacman_y + pacman_radius * math.cos(-mouth_angle)),
            ]
        )
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()