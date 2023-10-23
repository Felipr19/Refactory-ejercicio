import pygame
import math

pygame.init()

WIDTH, HEIGHT = 2200, 2000

YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Triángulo Rotante")

x, y = WIDTH // 2, HEIGHT // 2
angle = 0
speed = 0

triangle_size = 100

rotation_speed = 1
deceleration = 0.99
acceleration = 100

def draw_triangle(x, y, angle):
    triangle_points = [
        (x + triangle_size * math.cos(math.radians(angle)), y - triangle_size * math.sin(math.radians(angle))),
        (x + (triangle_size / 2) * math.cos(math.radians(angle - 120)), y - (triangle_size / 2) * math.sin(math.radians(angle - 120))),
        (x + (triangle_size / 2) * math.cos(math.radians(angle + 120)), y - (triangle_size / 2) * math.sin(math.radians(angle + 120)))
    ]
    pygame.draw.polygon(screen, YELLOW, triangle_points)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        angle += rotation_speed
    if keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    if keys[pygame.K_UP]:
        speed = min(8, speed + acceleration)
    else:
        speed *= deceleration
        if abs(speed) < 0.01:
            speed = 0

    x += speed * math.cos(math.radians(angle))
    y -= speed * math.sin(math.radians(angle))

    if x > WIDTH:
        x = 0
    elif x < 0:
        x = WIDTH
    if y > HEIGHT:
        y = 0
    elif y < 0:
        y = HEIGHT

    screen.fill((0, 0, 0))

    draw_triangle(x, y, angle)

    pygame.display.flip()

pygame.quit()
