import random

class Asteroid:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def move(self):
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)

# Create multiple asteroids
asteroids = []
for _ in range(10):  # Create 10 asteroids
    asteroid = Asteroid(random.randint(0, 100), random.randint(0, 100), random.randint(1, 3))
    asteroids.append(asteroid)

# Example of moving all asteroids
for asteroid in asteroids:
    asteroid.move()