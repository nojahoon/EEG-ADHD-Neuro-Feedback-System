import random, pygame, sys,time
from const import *

import sys


#이미지의 위치를 확인하는데 사용할 버튼클래스 : isOver사용
class button():
    def __init__(self,color,x,y,width,height,text=''):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
    def draw(self,win,outline=None):
        #call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win,outline,(self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),0)

        if self.text !='':
            font=pygame.font.SysFont('image/NanumGothic.ttf',30)
            text=font.render(self.text,1,(0,0,0))
            win.blit(text,(self.x+(self.width/2-text.get_width()/2),self.y+(self.height/2-text.get_height())))

    def isOver(self,pos):
        #pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y + self.height:
                return True
        return False

# 지정 위치 텍스트 출력
def Show_text(x, y, text):
    #pygame 내장 폰트 사용시 font.SysFont, 하지만 한글 출력시 font.Font 로 한글 폰트 사용해야함.
    sf = pygame.font.Font('font/CookieRun Bold.ttf', 50, bold=True)
    title_str = text
    title = sf.render(title_str, True, white)
    title_size = sf.size(title_str)
    title_pos = (x, y)
    screen.blit(title, title_pos)

#image Size변환하여 Showing
def Show_Image_Transform_Size(position_x,position_y,image,imageWidth,imageHeight):
    img = pygame.transform.scale(image, (imageWidth, imageHeight))
    screen.blit(img, (position_x,position_y))

#image position x, y에 Showing
def Show_Image(position_x,position_y,image):
    screen.blit(image,(position_x,position_y))

##----이미지 넣는예시----##
#x,y position에 이미지 크기 조정해서 넣는 함수
#Show_Image_Transform_Size(100,100,img,200,700)
#x,y position에 맞게 넣는 함수
#Show_Image(300,300,img)
##-----------------------##

img = pygame.image.load("Images/githubImage.jpg")

run = True

pygame.init()
pygame.display.set_caption("EEG ADHD Neuro Feedback Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200



clock = pygame.time.Clock()

gamestate=GAME_LOBBY

while run:
    screen.fill(black)


    pygame.draw.rect(screen, white,(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2, 100, 100))    #정사각형 그림그려주는 것
    Show_Image_Transform_Size(200, 200, img, 100, 100)                                  #이미지 삽입해주는 것
    Button0 = button((0, 255, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, 100)  # 이미지를 삽입한곳과 똑같은 버튼을 만들어 해당 이미지를 클릭했을 때 이벤트가 발생할 수 있게 함.
    Button1 = button((0, 255, 0), 200, 200, 100, 100)                               # 버튼을 삽입한곳과 똑같은 버튼을 만들어 해당 이미지를 클릭했을 때 이벤트가 발생할 수 있게 함.


    #어떤 화면인지 판가름하게 해주는 state를 나중에 만들어줄 생각
    # if (GAME_LOBBY==state) : 로비화면일때
    # elif (GAME_PLAY==state) : 진행단계일때
    # elif (GAME_PAUSE==sate) : 멈춤단계일때
    # elif (GAME_END==state) : 종료단계일때

    if(GAME_LOBBY==1):  #로비일때: GAME_LOBBY 진행단계일때
        Show_text(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 4, "색상 게임에 오신것을 환영합니다.")
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False;
            if (event.type == pygame.MOUSEBUTTONDOWN):  # and event.type == pygame.MOUSEBUTTONDOWN
                    Show_text(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 5, "마우스 눌렸음!!")
                    pos = pygame.mouse.get_pos()
                    if Button0.isOver(pos):
                        print('Clickevent')
                    if Button1.isOver(pos):
                        print('ImageClick')
            if not hasattr(event, 'key'): # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
                continue;


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 애플리케이션을 종료하고자 하면
            run = False;
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if not hasattr(event, 'key'):  # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
            continue
    clock.tick(60)
    pygame.display.flip()

pygame.quit()