import pygame
import time
import random
import sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

block_size = 10
FPS = 20

head = pygame.image.load("head.png")

if len(sys.argv) == 3 and sys.argv[1] == "debug":
    FPS = int(sys.argv[2])

font = pygame.font.SysFont("consolas", 20)

def message_to_screen(msg, color=black, wid=0, hei=0):
    screen_text = font.render(msg, True, color)

    gameDisplay.blit(screen_text, [display_width/2+wid, display_height/2+hei])


def snake(snakelist, lead_x, lead_y, head):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])
        gameDisplay.blit(head, [lead_x, lead_y])


def gameLoop(head):
    gameExit = False
    gameOver = False

    snakeList = []
    snakeLength = 1

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    last_button = None

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
                        gameLoop(head)
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not last_button == "RIGHT":
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, 90)
                    snakeList[0] == head
                    lead_y_change = 0
                    lead_x_change = -block_size
                    last_button = "LEFT"
                elif event.key == pygame.K_RIGHT and not last_button == "LEFT":
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, -90)
                    snakeList[0] == head
                    lead_y_change = 0
                    lead_x_change = block_size
                    last_button = "RIGHT"
                elif event.key == pygame.K_UP and not last_button == "DOWN":
                    head = pygame.image.load("head.png")
                    snakeList[0] == head
                    lead_x_change = 0
                    lead_y_change = -block_size
                    last_button = "UP"
                elif event.key == pygame.K_DOWN and not last_button == "UP":
                    head = pygame.image.load("head.png")
                    head = pygame.transform.rotate(head, 180)
                    snakeList[0] == head
                    lead_x_change = 0
                    lead_y_change = block_size
                    last_button = "DOWN"
                elif event.key == pygame.K_q:
                    gameOver = True
                    gameExit = True
                elif event.key == pygame.K_r:
                    gameExit = True
                    gameLoop()
                # elif event.key == pygame.K_EQUALS:
                #     snakeLength += 1

        
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        # print(lead_x, lead_y)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(snakeList, lead_x, lead_y, head)

        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength += 1

        clock.tick(FPS)

gameLoop(head)
