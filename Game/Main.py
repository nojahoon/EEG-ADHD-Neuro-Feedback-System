import random, pygame, sys,time

from const import *
from Imageload import *

# 지정 위치 텍스트 출력
def Show_text(x, y, text):
    #sf = pygame.font.SysFont("Monospace", 50, bold = True)
    sf = pygame.font.Font('font/CookieRun Bold.ttf', 30, bold=True)
    #pygame.font.Font('image/CookieRun Bold.ttf', heightSize // size)
    title_str = text
    title = sf.render(title_str, True, white)
    title_size = sf.size(title_str)
    title_pos = (x - title_size[0] // 2, y - title_size[1] // 2)
    screen.blit(title, title_pos)

def Show_img(x, y, img):
    img_size = img.get_size()
    screen.blit(img, (x - img_size[0] // 2, y - img_size[1] // 2))

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

white = (255, 255, 255)
black = (0, 0, 0)

run = True

pygame.init()
pygame.display.set_caption("EEG ADHD Neuro Feedback Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_scene = GAME_LOBBY

clock = pygame.time.Clock()
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 애플리케이션을 종료하고자 하면
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        # 마우스 누를 때 색 변경
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 로비 START 버튼
            if event.pos[0] > 300 and event.pos[0] < 700 and event.pos[1] > 525 and event.pos[1] < 675:
                if game_scene == GAME_LOBBY:
                    game_start_btn_img.fill((200, 200, 200))

        # 마우스 땔 때 씬 이동
        if event.type == pygame.MOUSEBUTTONUP:
            # 로비 START 버튼
            if event.pos[0] > 300 and event.pos[0] < 700 and event.pos[1] > 525 and event.pos[1] < 675:
                if game_scene == GAME_LOBBY:
                    game_scene = GAME_PLAY


    if game_scene == GAME_LOBBY:
        screen.fill(black)
        Show_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, "색상 게임에 오신것을 환영합니다.")
        Show_img(500, 600, game_start_btn_img)
        Show_img(1100, 600, game_quit_btn_img)
    elif game_scene == GAME_PLAY:
        screen.fill(black)
        Show_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, "게임 플레이!")

    #elif game_scene == GAME_PAUSE:

    #elif game_scene == GAME_END:


    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()