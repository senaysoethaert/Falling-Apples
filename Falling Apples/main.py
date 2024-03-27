import pygame

pygame.init()


infoObj = pygame.display.Info()
screen = pygame.display.set_mode((infoObj.current_w, infoObj.current_h))
running = True

#background = pygame.image.load('graphics/background-test.webp')
basket_img = pygame.image.load('graphics/picnic-basket.png').convert_alpha()
basket_img = pygame.transform.scale(basket_img, (200, 200))
basket_rect = basket_img.get_rect(midbottom=(1200,1200))

#basketPos =
grassColor = (0,128,0)

clock = pygame.time.Clock()

while running:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    #Stop game with escape button
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            exit()

    #Get mouse position    
    mousePos = pygame.mouse.get_pos()

    #Drawing of surfaces/images
    background = screen.fill((255,255,200))
    screen.blit(basket_img, (basket_rect))
    pygame.draw.rect(screen, grassColor, pygame.Rect(0, 1200, 3500, 1000))
    
    #Attach y and x coordinates of rect to mouse position
    basket_rect.x, basket_rect.y = mousePos
    basket_rect.x -= basket_rect.width / 2
    

    if mousePos[1] < infoObj.current_h:
        basket_rect.y = 1000
    
    pygame.display.update()


