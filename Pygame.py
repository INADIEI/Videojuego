import pygame

pygame.init()

ventana = pygame.display.set_mode((840,680))
pygame.display.set_caption("Ejemplo 1")

ball = pygame.image.load("C:/Users/USUARIO/Downloads/ball2.png")
ballrect = ball.get_rect()
speed = [4,4]
ballrect.move_ip(0,0)

bate = pygame.image.load("C:/Users/USUARIO/Downloads/bate.png")
baterect = bate.get_rect()
baterect.move_ip(240,450)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando==False

            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    
        
    ventana.fill((255,255,255))
    ventana.blit(ball, ballrect)
    ventana.blit(bate,baterect)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

## Notas de tu primo Sebas:
## Las imagenes hay que crearlas y editarlas, sacarlas de internet va a estar feo
## El juego aun no finaliza si te equivocas, la ventana no cierra y no hay score
## juego extraido de una pagina web no propia
