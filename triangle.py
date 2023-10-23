import math
import pygame

class Triangle:
    def __init__(self, x, y, size):
        # Initialize the triangle with given position, size, and initial values
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        self.speed = 0

    def rotate(self, rotation_speed):
        # Rotate the triangle by adding the specified rotation speed to the current angle
        self.angle += rotation_speed

    def move(self, acceleration, deceleration):
        # Move the triangle by adjusting its speed, position, and applying deceleration
        # The triangle's speed is limited to 8 and is increased by acceleration
        # Deceleration is applied to gradually slow down the triangle when no keys are pressed
        self.speed = min(8, self.speed + acceleration) if self.speed < 8 else self.speed
        self.speed *= deceleration
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))
