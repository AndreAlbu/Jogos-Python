import pygame
import random
from pygame.locals import *

def on_grid_random():

    x = random.randint(0, 590)
    y = random.randint(0, 590)

    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):

    return (c1[0] == c2[0]) and (c1[1] == c2[1])

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cobra")


font = pygame.font.SysFont(None, 55)

cobra = [(200,200), (210, 200), (220, 200)]

cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

direcao = ESQUERDA

clock = pygame.time.Clock()

while True:

    clock.tick(30)

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

        if event.type == KEYDOWN:

            if event.key == K_w:

                direcao = CIMA

            if event.key == K_s:

                direcao = BAIXO

            if event.key == K_d:

                direcao = DIREITA

            if event.key == K_a:

                direcao = ESQUERDA

    if colisao(cobra[0], apple_pos):

        apple_pos = on_grid_random()

        cobra.append((0,0))

    if colisao(cobra[0], cobra[1]):

        pygame.display.set_caption('Game Over')
        pygame.display.flip()

    for i in range(len(cobra) - 1, 0, -1):

        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])


    if direcao == CIMA:

        cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if direcao == DIREITA:

        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

    if direcao == BAIXO:

        cobra[0] = (cobra[0][0], cobra[0][1] + 10)

    if direcao == ESQUERDA:

        cobra[0] = (cobra[0][0]  - 10, cobra[0][1]) 
   
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for posicao in cobra:

        screen.blit(cobra_skin, posicao)

    pygame.display.update()


