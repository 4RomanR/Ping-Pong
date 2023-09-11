import pygame, sys
pygame.init()

black = (0,0,0)
yell = (250,220, 0)
blue = (50,80,250)
red =  (240,0,40)

screen_size = (800, 600)

player_width = 15
player_heigth = 30

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False

#Player 1
player_1_x_coor = 50
player_1_y_coor = 255
player_1_y_speed = 0
#Player 2
player_2_x_coor = 750 - player_width
player_2_y_coor = 255
player_2_y_speed = 0
#BALL
ball_x = 400
ball_y = 300
ball_x_speed = 3
ball_y_speed = 3

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #MOVIMIENTO PLAYER 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_1_y_speed = -3
            if event.key == pygame.K_s:
                player_1_y_speed = 3
    #MOVIMIENTO PLAYER 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player_2_y_speed = 3

    #MOVIMIENTO PLAYER 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_1_y_speed = 0
            if event.key == pygame.K_s:
                player_1_y_speed = 0
    #MOVIMIENTO PLAYER 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player_2_y_speed = 0

    player_1_y_coor += player_1_y_speed
    player_2_y_coor += player_2_y_speed

    #COLOCAR PAREDES 
    #------------------------------
    #COLOCAR PAREDES 
    
    ball_x += ball_x_speed
    ball_y += ball_y_speed  

    if ball_y > 590 or ball_y < 10:
        ball_y_speed *= -1
    if ball_x > 800 or ball_x < 10:
        ball_x_speed *= -1
    if ball_x > 800 and ball_x < 0:
        ball_x = 400
        ball_y = 300
        ball_x_speed *= -1
        ball_y_speed *= -1


    screen.fill(black)
#ZONA DE DIBUJO
    player_1 = pygame.draw.rect(screen, yell, (player_1_x_coor, player_1_y_coor, player_width, player_heigth))
    player_2 = pygame.draw.rect(screen, blue, (player_2_x_coor, player_2_y_coor, player_width, player_heigth))

    #BALL
    ball = pygame.draw.circle(screen, red, (ball_x, ball_y),10)
    #COLISIONES
    if ball.colliderect(player_1) or ball.colliderect(player_2 ):
        ball_x_speed *= -1
    pygame.display.flip() 
    clock.tick(60)
pygame.QUIT()

