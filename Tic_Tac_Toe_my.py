import pygame
from pygame.locals import *

pygame.init()
 
screen_w=300
screen_h=300
screen=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('WELCOME TO TIC TAC TOE GAME')

line_width=5
markers=[]
player=1
clicked =False
pos=(0,0)
winner=0
game_over=False

font=pygame.font.SysFont(None,40)

agn_rect=Rect(screen_w//2-80,screen_h//2,170,50)

green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)


for x in range(3):
    row=[0]*3
    markers.append(row)
print (markers)


def grid():
    bg= (228, 218, 199)
    grid_c=(0,0,0)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid_c,(0,x*100),(screen_w,x*100),line_width)
        pygame.draw.line(screen,grid_c,(x*100,0),(x*100,screen_h),line_width)



def draw_markers():
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),line_width)
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),line_width)

            if y==-1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),38,line_width)
            y_pos+=1
        x_pos+=1
        
def check_winner():
    global winner
    global game_over
    y_pos=0
    for x in markers:
        if(sum(x)==3):
            winner=1
            game_over=True
        if(sum(x)==-3):
            winner=2
            game_over=True

        if(markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==3):
            winner=1
            game_over=True
        if(markers[0][y_pos]+markers[1][y_pos]+markers[2][y_pos]==-3):
            winner=2
            game_over=True
        y_pos+=1
    
    if(markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==3 ):
        winner=1
        game_over=True
    if(markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==-3 ):
        winner=2
        game_over=True

    if game_over==False:
        tie=True
        for row in markers:
            for i in row:
                if i==0:
                    tie=False
        if tie==True:
            game_over=True
            winner=0

def print_winner(winner):
    if winner!=0:
        win_txt='Player '+str(winner)+' wins!!'
    elif winner==0:
         win_txt='Tie Match!'

    win_img=font.render(win_txt,True,blue)
    if winner==0:
        pygame.draw.rect(screen,green,(screen_w//2-100,screen_h//2-60,150,50))
    if winner==1:
        pygame.draw.rect(screen,green,(screen_w//2-100,screen_h//2-60,200,50))
    if winner==2:
        pygame.draw.rect(screen,red,(screen_w//2-100,screen_h//2-60,200,50))
    screen.blit(win_img,(screen_w//2-100,screen_h//2-50))

    txt=' Play again ?'
    img=font.render(txt,True,blue)
    pygame.draw.rect(screen,green,agn_rect)
    screen.blit(img,(screen_w//2-80,screen_h//2+10))





#main
run=True
while run:

    grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if game_over==False:
            if event.type== pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type== pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                cell_x=pos[0]//100
                cell_y=pos[1]//100
                if markers[cell_x][cell_y]==0:
                    markers[cell_x] [cell_y]=player
                    player*=-1
                    check_winner()
    if game_over==True:
        print_winner(winner)
        if event.type== pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked=True
        if event.type== pygame.MOUSEBUTTONUP and clicked==True:
            clicked=False
            pos=pygame.mouse.get_pos()
            if (agn_rect.collidepoint(pos)):
                markers=[]
                player=1
                clicked =False
                pos=[]
                winner=0
                game_over=False
                for x in range(3):
                    row=[0]*3
                    markers.append(row)
                print (markers)
    pygame.display.update()

pygame.quit()