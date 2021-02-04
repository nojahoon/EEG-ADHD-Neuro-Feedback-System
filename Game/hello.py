import random, pygame, sys,time
import sys

# 지정 위치 텍스트 출력
def Show_text(x, y, text):
    #sf = pygame.font.SysFont("Monospace", 50, bold = True)
    sf = pygame.font.Font('font/CookieRun Bold.ttf', 30, bold=True)
    #pygame.font.Font('image/CookieRun Bold.ttf', heightSize // size)
    title_str = text
    title = sf.render(title_str, True, white)
    title_size = sf.size(title_str)
    title_pos = (x, y)
    screen.blit(title, title_pos)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

white = (255, 255, 255)
black = (0, 0, 0)

run = True

pygame.init()
pygame.display.set_caption("EEG ADHD Neuro Feedback Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
while run:
    screen.fill(black)
    Show_text(SCREEN_WIDTH//2, SCREEN_HEIGHT//4, "색상 게임에 오신것을 환영합니다.")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 애플리케이션을 종료하고자 하면
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    clock.tick(60)
    pygame.display.flip()

pygame.quit()