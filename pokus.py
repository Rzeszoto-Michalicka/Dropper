import pygame
import random

#Zapnutie pygame
pygame.init()

#Obrazovka
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX,screenY))

#Prispôsobenie okna
pygame.display.set_caption("Dropper")
icon = pygame.image.load('down-arrow.png')
pygame.display.set_icon(icon)

#Obrázky
heart1 = pygame.image.load('heart.png')
heart2 = pygame.image.load('heart.png')
heart3 = pygame.image.load('heart.png')
background = pygame.image.load('background.jpg')
playerIMG = pygame.image.load('player.png')
zero = pygame.image.load('0.png')
one = pygame.image.load('1.png')
curlyL = pygame.image.load('curlyL.png')
curlyR = pygame.image.load('curlyR.png')

#Zvuky (hoijáááá, äMňe)

#Hráč
playerX = 370
playerY = 535
playerXchange = 0
playerYchange = 0
score = 0
lives = 3

#Friend
friendlyList = [zero, one]
friendlyIMG = []
friendX = []
friendYchange = []
friendY = []
numOfFriends = 2
friendlySpawn = 0

for i in range(numOfFriends):
    friendlyIMG.append(random.choice(friendlyList))
    friendX.append(random.randint(1, 731))
    friendYchange.append(0.25)
    friendY.append(friendlySpawn)
    friendlySpawn -= 350

#Enemy
enemyList = [curlyL, curlyR]
enemyIMG = []
enemyX = []
enemyYchange = []
enemyY = []
numOfEnemies = 2
enemySpawn = -200

for j in range(numOfEnemies):
    enemyIMG.append(random.choice(enemyList))
    enemyX.append(random.randint(1, 731))
    enemyYchange.append(0.25)
    enemyY.append(enemySpawn)
    enemySpawn -= 350

#Funkcie
def player(x, y):
    screen.blit(playerIMG, (x, y))

def friend(x, y):
    screen.blit(friendlyIMG[i], (x, y))

def enemy(x, y):
    screen.blit(enemyIMG[j], (x, y))

def isCollision(playerY, friendY, friendX):
    if playerY == friendY[i] and friendX[i] in range(playerX-55, playerX+55):
        return True
    if playerY == friendY[i] and friendX[i] not in range(playerX-55, playerX+55):
        return False

def isCollisionEnemy(playerY, enemyY, enemyX):
    if playerY == enemyY[j] and enemyX[j] in range(playerX-55, playerX+55):
        return True
    if playerY == enemyY[j] and enemyX[j] not in range(playerX-55, playerX+55):
        return False


#Loop celej hry
run = True
while run:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Pohyb
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -1
            if event.key == pygame.K_RIGHT:
                playerXchange = +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    #Friend pohyb
    for i in range(numOfFriends):
        friendY[i] += friendYchange[i]
    
    #Enemy pohyb
    for j in range(numOfEnemies):
        enemyY[j] += enemyYchange[j]
    
    screen.blit(background, (0, 0))
    
    if lives == 3:
        screen.blit(heart1, (750, 0))
        screen.blit(heart2, (715, 0))
        screen.blit(heart3, (680, 0))
    elif lives == 2:
        screen.blit(heart1, (750, 0))
        screen.blit(heart2, (715, 0))
    elif lives == 1:
        screen.blit(heart1, (750, 0))
    elif lives < 1:
        run = False               
    

    #Kolízia friends
    for i in range(numOfFriends):
        
        collision = isCollision(playerY, friendY, friendX)
        if collision == True:
            friendX[i] = (random.randint(1, 730))
            friendY[i] = 0
            score += 1
            print("boom")
            friendlyIMG[i] = random.choice(friendlyList)
        if collision == False:
            friendX[i] = (random.randint(1, 730))
            friendY[i] = 0
            lives -= 1
            print("vedla")
            friendlyIMG[i] = random.choice(friendlyList)

    #Kolízia enemy
    for j in range(numOfEnemies):
        
        collisionEnemy = isCollisionEnemy(playerY, enemyY, enemyX)
        if collisionEnemy == True:
            enemyX[j] = (random.randint(1, 730))
            enemyY[j] = 0
            lives -= 1
            print("zasah")
            enemyIMG[j] = random.choice(enemyList)
        if collisionEnemy == False:
            enemyX[j] = (random.randint(1, 730))
            enemyY[j] = 0            
            enemyIMG[j] = random.choice(enemyList)

    playerX += playerXchange
    for i in range(numOfFriends):
        friend(friendX[i], friendY[i])
    for j in range(numOfEnemies):
        enemy(enemyX[j], enemyY[j])
    player(playerX, playerY)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    pygame.display.update()
