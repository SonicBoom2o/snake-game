import pygame
import time
import random
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

# Head
head = pygame.image.load("head.png")

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Slither")

clock = pygame.time.Clock()

block_size = 10
FPS = 20

if len(sys.argv) == 3 and sys.argv[1] == "debug":
    FPS = int(sys.argv[2])

font = pygame.font.SysFont("consolas", 20)

def message_to_screen(msg, color=black, wid=0, hei=0):
    screen_text = font.render(msg, True, color)

    gameDisplay.blit(screen_text, [display_width/2+wid, display_height/2+hei])


def gameLoop(head):
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    while not gameExit:     
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Press Q to quit or C to continue", wid=-170)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, 90)
                    lead_y_change = 0
                    lead_x_change = -block_size
                if event.key == pygame.K_RIGHT:
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, -90)
                    lead_y_change = 0
                    lead_x_change = block_size
                if event.key == pygame.K_UP:
                    head = pygame.image.load("head.png")
                    lead_x_change = 0
                    lead_y_change = -block_size
                if event.key == pygame.K_DOWN:
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, 180)
                    lead_x_change = 0
                    lead_y_change = block_size
                if event.key == pygame.K_q:
                    gameOver = True
                    gameExit = True
                if event.key == pygame.K_r:
                    gameExit = True
                    gameLoop()

        
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red,[randAppleX, randAppleY, block_size, block_size])
        # pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
        gameDisplay.blit(head, [lead_x, lead_y])
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            print("Om nom nomn")

        clock.tick(FPS)

gameLoop(head)
