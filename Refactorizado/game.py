import math
import pygame
from triangle import *

class Game:
    def __init__(self, width, height, triangle_size, rotation_speed, acceleration, deceleration):
        # Initialize the game with specified parameters
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rotating Triangle")
        self.YELLOW = (255, 255, 0)
        self.clock = pygame.time.Clock()
        self.triangle = Triangle(self.WIDTH // 2, self.HEIGHT // 2, triangle_size)
        self.rotation_speed = rotation_speed
        self.acceleration = acceleration
        self.deceleration = deceleration

    def draw_triangle(self, triangle):
        # Draw the triangle on the screen based on its current position and angle
        triangle_points = [
            (triangle.x + triangle.size * math.cos(math.radians(triangle.angle)), triangle.y - triangle.size * math.sin(math.radians(triangle.angle))),
            (triangle.x + (triangle.size / 2) * math.cos(math.radians(triangle.angle - 120)), triangle.y - (triangle.size / 2) * math.sin(math.radians(triangle.angle - 120))),
            (triangle.x + (triangle.size / 2) * math.cos(math.radians(triangle.angle + 120)), triangle.y - (triangle.size / 2) * math.sin(math.radians(triangle.angle + 120)))
        ]
        pygame.draw.polygon(self.screen, self.YELLOW, triangle_points)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                # Rotate the triangle to the left when the left arrow key is pressed
                self.triangle.rotate(self.rotation_speed)
            if keys[pygame.K_RIGHT]:
                # Rotate the triangle to the right when the right arrow key is pressed
                self.triangle.rotate(-self.rotation_speed)

            if keys[pygame.K_UP]:
                # Move the triangle forward when the up arrow key is pressed
                self.triangle.move(self.acceleration, 1)
            else:
                # Apply deceleration when no arrow keys are pressed to gradually slow down the triangle
                self.triangle.move(0, self.deceleration)

            self.screen.fill((0, 0, 0))
            self.draw_triangle(self.triangle)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
