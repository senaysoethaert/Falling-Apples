import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

infoObj = pygame.display.Info()
screen = pygame.display.set_mode((infoObj.current_w, infoObj.current_h))
running = True

# Load images
apple_img = pygame.image.load('graphics/apple.png').convert_alpha()
apple_img = pygame.transform.scale(apple_img, (70,70))
apple_rect = apple_img.get_rect(midtop=(1200,10))
apple_rect.y = 0

basket_img = pygame.image.load('graphics/picnic-basket.png').convert_alpha()
basket_img = pygame.transform.scale(basket_img, (200, 200))
basket_rect = basket_img.get_rect(midbottom=(200,200))

# Load audio
bg_music = pygame.mixer.music.load('audio/Hay Day - Main Theme.mp3')

# Colors
grassColor = (0,128,0)
BLACK = (0,0,0)

# Gravity/velocity
velocity = 6

# Text/score
score_count = 0

clock = pygame.time.Clock()

# Start playing background music
pygame.mixer.music.play()

while running:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    # Stop game with escape button
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            exit()

    # Get mouse position    
    mousePos = pygame.mouse.get_pos()

    basket_rect_mouse = basket_rect.copy()
    basket_rect_mouse.width, basket_rect_mouse.height = 200, 50
    basket_rect_mouse.y += 160  # Move 10 pixels up

    # Drawing of surfaces/images
    background = screen.fill((255,255,200))
    apple = screen.blit(apple_img, (apple_rect))
    basket = screen.blit(basket_img, (basket_rect))
    grass = pygame.draw.rect(screen, grassColor, pygame.Rect(0, 1200, 3500, 1000))
    font = pygame.font.SysFont(None, 50)
    text = font.render(f'Score: {score_count}', False, BLACK)
    score = screen.blit(text, dest=(10,10))
    
    # Attach y and x coordinates of rect to mouse position
    basket_rect.x, basket_rect.y = mousePos
    basket_rect.x -= basket_rect.width / 2
    apple_rect.y += velocity

    # If apple collides with basket, make apple fall faster cycle
    if apple_rect.colliderect(basket_rect_mouse):    
        apple_rect.x = random.randint(0, infoObj.current_w)
        apple_rect.y = 0
        velocity += 1
        score_count += 1
    elif apple_rect.colliderect(grass):
        exit()

    if mousePos[1] < infoObj.current_h:
        basket_rect.y = 1000
    
    pygame.display.update()


