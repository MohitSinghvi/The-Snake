
'''Python project
   Topic : Snake Game

'''

import pygame ,time, random

# Defining colours
white = (255,255,255)
black= (0,0,0)
red= (255,0,0)
blue=(0,0,255)
green=(0,255,0)

pygame.init()

#for setting the title
pygame.display.set_caption('The Snake')

game_width=800
game_height=650
screen_width=798
screen_height=550

window=pygame.display.set_mode((game_width,game_height))

speed=10
count=-1

fps=30
clock=pygame.time.Clock()

#Font
font=pygame.font.Font(None,25)

#function to display text on the screen
def msgToScrn(msg,color,mx,my,size=25):
    font = pygame.font.Font(None, size)
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[mx,my])

#function to take the name of the player
def takeName(player):
    nameTaken=False
    player_name=list(player)
    capital=False

    while nameTaken==False:
        window.fill(white)
        msgToScrn("Enter Name :", red, int(screen_width / 4)+100, int(screen_height / 2),50)
        msgToScrn(player,black,int(screen_width / 4)+100,int(screen_height / 2)+100,50)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nameTaken=True
                break
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    nameTaken=True
                    f=open('name.txt','w+')
                    f.write(player)
                    f.close()
                    break
                elif event.key==pygame.K_DELETE:
                    player_name=[]
                    player = "".join(player_name)
                elif event.key==pygame.K_BACKSPACE and len(player_name)!=0:
                    player_name.pop()
                    player = "".join(player_name)
                elif event.key==pygame.K_SPACE:
                    player_name.append(" ")
                    player = "".join(player_name)
                elif event.key==pygame.K_RSHIFT or event.key==pygame.K_LSHIFT:
                    capital=True
                elif event.key==pygame.K_CAPSLOCK:
                    if(capital==False):
                        capital=True
                    else:
                        capital=True
                elif event.key!=pygame.K_BACKSPACE and event.key!=pygame.K_LSHIFT and event.key!=pygame.K_RSHIFT:
                    if(capital==True):
                        if event.key==pygame.K_MINUS:
                            player_name.append("_")
                            player = "".join(player_name)
                        else:
                            player_name.append(pygame.key.name(event.key).upper())
                            player = "".join(player_name)
                    else:
                        player_name.append(pygame.key.name(event.key))
                        player="".join(player_name)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RSHIFT or event.key==pygame.K_LSHIFT:
                    capital=False

#Function to get the highscore saved in a file
def getHighScore():
    f = open('score.txt', 'r+')
    high_score = f.read()

    f.close()

    f=open('scorer.txt','r+')
    high_scorer = f.read()
    f.close()
    return high_scorer,high_score

#function to display the highscore
def putHighScore(highscorer,highscore):
    showHiScore=True
    while showHiScore==True:
            window.fill(white)
            msgToScrn("HIGH SCORE ", red, int(screen_width / 4)-100, int(screen_height / 2)-200,50)
            msgToScrn("Player Name : " + highscorer , blue, int(screen_width / 4)-100,
                      int(screen_height / 2)-100,50)
            msgToScrn("SCORE : " + highscore,blue, int(screen_width / 4)-100,
                      int(screen_height / 2),50)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        showHiScore=False

#This is game loop which ensures the game is progressing
def gameLoop():
    lead_x = int(screen_width / 2)
    lead_y = int(screen_height / 2)
    old_x = []
    old_y = []
    HS=0
    game_play=False
    gameExit = False
    gameOver=False
    action = "right"
    count = 0
    i = 0
    fps = 15
    pause=False
    pressed=True
    epressed=False
    level=1
    f = open('name.txt', 'r+')
    player = f.read()
    f.close()
    msx=int(screen_width/2)-100
    msy=int(screen_height / 2)
    msrectcol=[white,white,white,white,white,white]
    mscol = [black,black,black,black,black,]
    kp=0
    msize=50

    #This Loop is the Initial Screen of the game,i.e when the game is not started.
    while game_play==False:

        window.fill(white)

        msgToScrn("~~~~~~              ~~~~~~~~",blue,0,msy-150,100)

        msgToScrn("             SNAKE ", red, 0, msy - 150, 100)
        pygame.draw.rect(window, msrectcol[0], [msx, msy-50, 250, 50])
        msgToScrn(" New Game ",mscol[0],msx, msy-50, msize)

        pygame.draw.rect(window,msrectcol[1], [msx,msy , 250, 50])
        msgToScrn(" High Score ",mscol[1],msx , msy, msize)

        pygame.draw.rect(window, msrectcol[2], [msx, msy+ 50, 250, 50])
        msgToScrn(" Reset Name ",mscol[2],msx, msy+50, msize)

        pygame.draw.rect(window,msrectcol[3], [msx,msy + 100, 250, 50])
        msgToScrn(" QUIT ", mscol[3], msx, msy + 100,msize)

        msgToScrn("~~~~~~~~~~~~~~~~~~~~~",red,0, msy +200, 100)
        msgToScrn("~~~~~~~~~~~~~~~~~~~~~", blue, 0, msy + 250, 100)
        pygame.display.update()



        if gameExit==True:
            break

        #Event Handling using Keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                break
            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_DOWN:
                    kp+=1
                    if(kp>3):
                        kp=0
                    pressed=True
                if event.key==pygame.K_UP:
                    kp-=1
                    if(kp<0):
                        kp=3
                    pressed=True
                if event.key==pygame.K_RETURN:
                    epressed=True


            if event.type==pygame.MOUSEMOTION or (pressed==True ) :
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(msx,msx+250)  or (kp<4):

                    if (mouse_y in range(msy-50,msy) and mouse_x in range(msx,msx+250) )  or (kp==0):
                        if(pressed==False):
                            kp=0
                        msrectcol[0]=black
                        mscol[0]=white
                    else:
                        msrectcol[0]= white
                        mscol[0] = red
                    if (mouse_y in range(msy,msy+50) and mouse_x in range(msx,msx+250) ) or (kp==1 and pressed==True):
                        if (pressed == False):
                            kp = 1
                        msrectcol[1] = black
                        mscol[1] = white
                    else:
                        msrectcol[1] = white
                        mscol[1] = red
                    if (mouse_y in range(msy+50,msy+100)and mouse_x in range(msx,msx+250) ) or (kp==2 and pressed==True):
                        if (pressed == False):
                            kp = 2
                        msrectcol[2] = black
                        mscol[2] = white
                    else:
                        msrectcol[2] = white
                        mscol[2] = red

                    if (mouse_y in range(msy+100,msy+150)and mouse_x in range(msx,msx+250) ) or (kp==3 and pressed==True):
                        if (pressed == False):
                            kp = 3
                        msrectcol[3] = black
                        mscol[3] = white
                    else:
                        msrectcol[3] = white
                        mscol[3] = red

                else:
                    msrectcol = [white,white,white,white,white,white]
                    mscol=[black,black,black,black,black,]
                pressed=False

            elif event.type==pygame.MOUSEBUTTONDOWN  or epressed==True:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(msx,msx+250) or epressed==True:
                    if mouse_y in range(msy-50,msy) or (kp==0):
                        game_play = True

                        break
                    if mouse_y in range(msy,msy+50)or (kp==1):
                        high_scorer, high_score = getHighScore()
                        putHighScore(high_scorer, high_score)
                    if mouse_y in range(msy+50,msy+100) or (kp==2):
                        f = open('name.txt', 'r+')
                        player = f.read()
                        f.close()
                        takeName(player)

                    if mouse_y in range(msy+100,msy+150) or (kp==3):
                        gameExit = True
                epressed=False

    #This loop gets executed when the player Decides to start playing the game
    while gameExit==False :
        if count>10:
            level=2

        #This loop gets executed when the player pauses the game
        while pause==True:
            window.fill(white)


            msgToScrn("<space>     ===>Resume ", green,100, int(screen_height / 2) - 50, 35)
            msgToScrn("R                 ===>Restart ", red, 100, int(screen_height / 2), 35)
            msgToScrn("H                 ===>HighScore ", blue, 100, int(screen_height / 2) + 50, 35)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pause=False
                    break
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        pause=False
                        break
                    if event.key==pygame.K_r:
                        gameLoop()
                    if event.key==pygame.K_h:
                        high_scorer,high_score=getHighScore()
                        putHighScore(high_scorer,high_score)
            msgToScrn("Score = " + str(count - 1), red, 700, 600)

            pygame.display.update()
        #this loop gets execute when the player loses
        while gameOver == True:
            time.sleep(1)
            window.fill(white)

            f=open('name.txt','r+')
            player=f.read()
            f.close()

            f = open('score.txt', 'r+')
            previous_highscore = f.read()

            f.close()
            if (count-1 > int(previous_highscore)):
                f=open('scorer.txt','w+')
                f.write(player)
                f.close()

                f = open('score.txt', 'w+')
                f.write(str(count-1))

                f.close()
                HS=1

            high_scorer,high_score = getHighScore()

            if(HS==1):
                msgToScrn("Congatulations HighScore!! ", black, 20, int(screen_height / 2) - 250, 80)

            msgToScrn("Game Over :( ", red, 20, int(screen_height / 2) -200, 100)
            msgToScrn(player+"'s Score : "+str(count-1),red, 20, int(screen_height / 2) - 50, 35)
            msgToScrn("Highscorer => "+high_scorer+" : "+high_score, blue, 20, int(screen_height / 2) - 0, 35)
            msgToScrn("ENTER : PLAY AGAIN ", blue, 20, int(screen_height / 2)+50, 35)
            msgToScrn("Q : QUIT", blue, 20, int(screen_height / 2) + 100, 35)


            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameOver = False
                        gameLoop()

                    elif event.key == pygame.K_q:

                        gameExit=True
                        gameOver=False


        window.fill(white)
        if level==1:
            pygame.draw.rect(window,green, [1, 1, screen_width, screen_height+10], 1)
            if lead_x < 0:
                lead_x = screen_width
            elif lead_x > screen_width-10:
                lead_x = 0
            if lead_y < 0:
                lead_y = screen_height
            elif lead_y >screen_height-10:
                lead_y = 0
        if level==2:
            pygame.draw.rect(window, red, [1,1,screen_width,screen_height],2)

            if lead_x < 0 or lead_x > screen_width-10 or lead_y < 0 or lead_y > screen_height-10:
                gameOver=True

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                gameExit=True

            # Controlling the snake with the keyboard
            if event.type == (pygame.KEYDOWN):
                if event.key==pygame.K_LEFT and action!="right":
                    action="left"
                    break

                elif event.key==pygame.K_RIGHT and action!="left":
                    action="right"
                    break

                elif event.key==pygame.K_UP and action!="down":
                    action="up"
                    break

                elif event.key==pygame.K_DOWN and action!="up":
                    action="down"
                    break
                elif event.key==pygame.K_SPACE:
                    if(pause==True):
                        pause=False
                    elif(pause==False):

                        pause=True

        if(pause==False ):
            if (action == "right" ):

                old_y.append(lead_y)
                old_x.append(lead_x)
                i = i + 1
                lead_x += speed
            elif (action == "left"):
                old_x.append(lead_x)
                old_y.append(lead_y)
                i += 1
                lead_x -= speed
            elif (action == "up"):
                old_y.append(lead_y)
                old_x.append(lead_x)
                i += 1
                lead_y -= speed
            elif (action == "down"):
                old_y.append(lead_y)
                old_x.append(lead_x)
                i += 1
                lead_y += speed

        for l in range(len(old_x)):
            if old_x[l] == lead_x:
                if old_y[l] == lead_y:
                    gameOver = True
                    break
        #To display the Head of the Screen
        if(gameOver==False):
            pygame.draw.rect(window,blue, [lead_x, lead_y, 10, 10])

            #To Display the body of the snake.
            for j in range(0,count):
                if len(old_x)!=0:
                    body_x=len(old_x)-1-j
                    body_y=len(old_y)-1-j
                    pygame.draw.rect(window, black, [old_x[body_x], old_y[body_y], 10, 10])

            if (pause == False):
                while(0<len(old_x)>=count):
                    old_x.pop(0)
                while(0 < len(old_y) >= count):
                    old_y.pop(0)

                #To generate the position of the item(food)
                if (count==0 or ((int(lead_x)-10)< random_x <(int(lead_x)+10) and (int(lead_y)-10)<random_y <(int(lead_y)+10)) ) :
                    random_x = random.randint(5, screen_width-5)
                    random_y = random.randint(5, screen_height-5)
                    count=count+1
                    fps=fps+0.2

                #To display the Food of the snake
                pygame.draw.rect(window, red, [random_x, random_y, 10, 10])
            msgToScrn(" Score = "+str(count-1),black,600,600)
            msgToScrn("Level: " + str(level), blue, 10, 600)
            msgToScrn("<space> : PAUSE/RESUME",black, 300, 600)
            msgToScrn("PLAYER : "+player,red,10,580)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameLoop()



