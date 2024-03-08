# Importing the libraries
import pygame
import random
from sys import getsizeof

# Initialize Pygame
pygame.init()

# Create Game Window
screenSize = 600
gridSize = 25
screen = pygame.display.set_mode((screenSize, screenSize))

# Title
pygame.display.set_caption("Snake")

# Colors
snakeColor = (0, 255, 0)
foodColor = (255, 0, 0)
bgColor = (0, 0, 0)
scoreTextColor = (255, 0, 0)

# Snake Properties
snakeSize = gridSize
snakeSpeed = 12
snakeX = screenSize / 2
snakeY = screenSize / 2
snakeXChange = 0
snakeYChange = 0
snakeList = [] # Snake Length = Size of List.
snakeLength = 1 # Starting Length of the Snake.
snakeDirection = "UP"

# Food Properties
foodSize = gridSize
foodX = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize
foodY = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize

# Score
playerScore = 0
font = pygame.font.Font(None, 36)

# Game Over
isGameOver = True

def restartGame():
    global isGameOver, snakeX, snakeY, snakeXChange, snakeYChange, snakeList, snakeLength, snakeSpeed, playerScore, foodX, foodY
    isGameOver = False
    snakeX = screenSize / 2
    snakeY = screenSize / 2
    snakeXChange = 0
    snakeYChange = 0
    snakeList = []
    snakeLength = 1
    snakeSpeed = 12
    playerScore = 0
    foodX = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize
    foodY = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize

# Game Loop
isGameOver = False
while not isGameOver:
    screen.fill(bgColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snakeDirection != "RIGHT":
                snakeXChange = -snakeSize
                snakeYChange = 0
                snakeDirection = "LEFT"
            elif event.key == pygame.K_RIGHT and snakeDirection != "LEFT":
                snakeXChange = snakeSize
                snakeYChange = 0
                snakeDirection = "RIGHT"
            elif event.key == pygame.K_UP and snakeDirection != "DOWN":
                snakeYChange = -snakeSize
                snakeXChange = 0
                snakeDirection = "UP"
            elif event.key == pygame.K_DOWN and snakeDirection != "UP":
                snakeYChange = snakeSize
                snakeXChange = 0
                snakeDirection = "DOWN"

    # Snake Movement
    snakeX += snakeXChange
    snakeY += snakeYChange

    # Check If Snake Hit Border
    if snakeX >= screenSize or snakeX < 0 or snakeY >= screenSize or snakeY < 0:
        isGameOver = True
        restartGame()

    # Snake Eating Food
    if snakeX == foodX and snakeY == foodY:
        foodX = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize
        foodY = round(random.randrange(0, screenSize - foodSize) / gridSize) * gridSize
        snakeLength += 1
        if playerScore >= 10:
            snakeSpeed += 1
        playerScore += 1

    # Snake Body
    snakeHead = []
    snakeHead.append(snakeX)
    snakeHead.append(snakeY)
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]

    for segment in snakeList[:-1]:
        if segment == snakeHead:
            isGameOver = True
            restartGame()

    # Draw Snake
    for segment in snakeList:
        pygame.draw.rect(screen, snakeColor, [segment[0], segment[1], snakeSize, snakeSize])

    # Draw Food
    pygame.draw.rect(screen, foodColor, [foodX, foodY, foodSize, foodSize])

    # Score
    scoreText = font.render(str(playerScore), True, (scoreTextColor))
    screen.blit(scoreText, (screenSize / 2, 600 - getsizeof(scoreText) / 2))
    
    # Update Game Window
    pygame.display.update()

    # Game Speed
    pygame.time.Clock().tick(snakeSpeed)

