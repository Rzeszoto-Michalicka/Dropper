import pygame
import random
import sys
from pygame import mixer
import json


#Zapnutie pygame
pygame.init()
gameStart = 1
login_data = {
    "nikos":1,
    "minerxx91":1,
}
try:
    with open("login_data.txt") as login_data_load:
        login_data = json.load(login_data_load)
    print(login_data)
except:
    print("No file created yet")

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
end = pygame.image.load("end.jpg")
newgame1 = pygame.image.load("button_newgame1.png")
newgame2 = pygame.image.load("button_newgame2.png")
quit1 = pygame.image.load("button_quit1.png")
quit2 = pygame.image.load("button_quit2.png")
button_newgame = newgame1
button_quit = quit1
gameover = pygame.image.load("gameover.png")
menuIMG = pygame.image.load("menu.png")
play1 = pygame.image.load("play1.png")
play2 = pygame.image.load("play2.png")
play = play1
hashtag = pygame.image.load("hashtag.png")
endless1 = pygame.image.load("mod_endless1.png")
endless2 = pygame.image.load("mod_endless2.png")
button_endless = endless2
levels1 = pygame.image.load("mod_levels1.png")
levels2 = pygame.image.load("mod_levels2.png")
button_levels = levels2

#Zvuky
pygame.mixer.init()
stellar = pygame.mixer.music.load("stellar.wav")
pygame.mixer.music.set_volume(0.25)

#Font
font = pygame.font.Font('freesansbold.ttf', 32)
base_font = pygame.font.Font(None, 32)

#Input pole
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

#Hráč
playerX = 370
playerY = 535
playerXchange = 0
playerYchange = 0
score_value = 0
lives = 3

#Friend
spawnFriend = [10, 110, 210, 310, 410, 510, 610, 710]
friendlyList = [zero, one]
friendlyIMG = []
friendX = []
friendYchange = []
friendY = []
numOfFriends = 2
friendlySpawn = 0

for i in range(numOfFriends):
    friendlyIMG.append(random.choice(friendlyList))
    friendX.append(random.choice(spawnFriend))
    friendYchange.append(0.25)
    friendY.append(friendlySpawn)
    friendlySpawn -= 300

#Enemy
spawnEnemy = [60, 160, 260, 360, 460, 560, 660, 650]
enemyList = [curlyL, curlyR, hashtag]
enemyIMG = []
enemyX = []
enemyYchange = []
enemyY = []
numOfEnemies = 2
enemySpawn = -150

for j in range(numOfEnemies):
    enemyIMG.append(random.choice(enemyList))
    enemyX.append(random.choice(spawnEnemy))
    enemyYchange.append(0.25)
    enemyY.append(enemySpawn)
    enemySpawn -= 300

#Funkcie
def player(x, y):
    screen.blit(playerIMG, (x, y))

def friend(x, y):
    screen.blit(friendlyIMG[i], (x, y))

def enemy(x, y):
    screen.blit(enemyIMG[j], (x, y))

def isCollisionFriends(playerY, friendY, friendX):
    if playerY == friendY[i] and friendX[i] in range(playerX-60, playerX+60):
        return True
    if playerY == friendY[i] and friendX[i] not in range(playerX-60, playerX+60):
        return False

def isCollisionEnemy(playerY, enemyY, enemyX):
    if playerY == enemyY[j] and enemyX[j] in range(playerX-55, playerX+55):
        return True
    if playerY == enemyY[j] and enemyX[j] not in range(playerX-55, playerX+55):
        return False

def start():
    global playerX
    global playerY
    global playerXchange
    global playerYchange
    global score_value
    global lives
    global spawnFriend
    global friendlyList
    global friendlyIMG 
    global friendX
    global friendYchange
    global friendY
    global numOfFriends
    global friendlySpawn
    global spawnEnemy
    global enemyList
    global enemyIMG
    global enemyX
    global enemyYchange
    global enemyY
    global numOfEnemies
    global enemySpawn
    global gameStart
    if gameStart == 1:
        #Hráč
        playerX = 370
        playerY = 535
        playerXchange = 0
        playerYchange = 0
        score_value = 0
        lives = 3

        #Friend
        spawnFriend = [10, 110, 210, 310, 410, 510, 610, 710]
        friendlyList = [zero, one]
        friendlyIMG = []
        friendX = []
        friendYchange = []
        friendY = []
        numOfFriends = 2
        friendlySpawn = 0

    for i in range(numOfFriends):
        friendlyIMG.append(random.choice(friendlyList))
        friendX.append(random.choice(spawnFriend))
        friendYchange.append(0.25)
        friendY.append(friendlySpawn)
        friendlySpawn -= 300

    if gameStart == 1:
        #Enemy
        spawnEnemy = [60, 160, 260, 360, 460, 560, 660, 650]
        enemyList = [curlyL, curlyR, hashtag]
        enemyIMG = []
        enemyX = []
        enemyYchange = []
        enemyY = []
        enemySpawn = -150
        gameStart = 2

    for j in range(numOfEnemies):
        enemyIMG.append(random.choice(enemyList))
        enemyX.append(random.choice(spawnEnemy))
        enemyYchange.append(0.25)
        enemyY.append(enemySpawn)
        enemySpawn -= 300


#Loop celej hry
decision = True
run = True
game = True
menu = True
active = False
while menu:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("login_data.txt", "w") as login_data_write:
                json.dump(login_data,login_data_write)
            run = False
            game = False
            menu = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
            if event.key == pygame.K_KP_ENTER:
                user_text = user_text[:-1]

    
    screen.blit(menuIMG, (0,0))
    screen.blit(play, (320, 260))
    mouse = pygame.mouse.get_pos()
    if mouse[0] in range(320, 470) and mouse[1] in range(260,360):
        play = play2
        if event.type == pygame.MOUSEBUTTONDOWN and user_text != "":
            login_data[user_text] = "1"
            print(login_data)
            menu = False
    elif mouse[0] not in range(320, 470) or mouse[1] not in range(260, 360):
        play = play1
    
    if active == True:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    
    pygame.display.update()  



while decision:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("login_data.txt", "w") as login_data_write:
                json.dump(login_data,login_data_write)
            run = False
            game = False
            menu = False
            decision = False

    screen.blit(end, (0, 0))
    screen.blit(button_endless, (450,200))
    screen.blit(button_levels, (150,200))
    mouse = pygame.mouse.get_pos()
    if mouse[0] in range(450, 650) and mouse[1] in range(200,400):
        button_endless = endless1
        if event.type == pygame.MOUSEBUTTONDOWN:
            decision = False         
    else:
        button_endless = endless2 

    if mouse[0] in range(150, 350) and mouse[1] in range(200,400):
        button_levels = levels1         
    else:
        button_levels = levels2 



    pygame.display.update()

pygame.mixer.music.play(-1)

while run: 

    screen.fill((0, 0, 0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("login_data.txt", "w") as login_data_write:
                json.dump(login_data,login_data_write)
            run = False
            game = False
    
    #Pohyb
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
                playerXchange = -1
        if event.key == pygame.K_RIGHT:
                playerXchange = +1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerXchange = 0


    if gameStart == 1:
        numOfEnemies = 2
        start()
    if gameStart == 2:
        if score_value > 10:
            numOfEnemies = 3
        if score_value > 20:
            numOfEnemies = 4
        start()    
    
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
        gameStart = 1
        run = False                  

    #Kolízia friends
    for i in range(numOfFriends):
        
        collisionFriends = isCollisionFriends(playerY, friendY, friendX)
        if collisionFriends == True:
            friendX[i] = (random.choice(spawnFriend))
            friendY[i] = 0
            score_value += 1
            print("boom")
            friendlyIMG[i] = random.choice(friendlyList)
        if collisionFriends == False:
            friendX[i] = (random.choice(spawnFriend))
            friendY[i] = 0
            lives -= 1
            print("vedla")
            friendlyIMG[i] = random.choice(friendlyList)

    #Kolízia enemies
    for j in range(numOfEnemies):
        
        collisionEnemy = isCollisionEnemy(playerY, enemyY, enemyX)
        if collisionEnemy == True:
            enemyX[j] = (random.choice(spawnEnemy))
            enemyY[j] = 0
            lives -= 1
            print("zasah")
            enemyIMG[j] = random.choice(enemyList)
        if collisionEnemy == False:
            enemyX[j] = (random.choice(spawnEnemy))
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

    score = font.render("Skóre : " + str(score_value), True, (58, 47, 214))
    screen.blit(score, (350, 0))


    pygame.display.update()

    while game == True and run == False:
        screen.blit(end, (0, 0))
        screen.blit(button_newgame, (272,200))
        screen.blit(button_quit, (272,400))
        screen.blit(gameover, (144,0))
        mouse = pygame.mouse.get_pos()
        if mouse[0] in range(282, 518)  and mouse[1] in range(210, 318):
            button_newgame = newgame2
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("newgame")
                run = True
                
                start()
        elif mouse[0] not in range(282, 518) and mouse[1] not in range(210, 318):
            button_newgame = newgame1
        
        if mouse[0] in range(282, 518)  and mouse[1] in range(410, 518):
            button_quit = quit2
            if event.type == pygame.MOUSEBUTTONDOWN:
                game = False
                run = False
        else:
            button_quit = quit1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("login_data.txt", "w") as login_data_write:
                    json.dump(login_data,login_data_write)    
                game = False
                run = False
        pygame.display.update()
