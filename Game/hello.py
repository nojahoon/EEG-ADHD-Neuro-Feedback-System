import random, pygame, sys,time
import sys

# 지정 위치 텍스트 출력
def Show_text(x, y, text):
    sf = pygame.font.SysFont("Monospace", 50, bold = True)
    title_str = text
    title = sf.render(title_str, True, white)
    title_size = sf.size(title_str)
    title_pos = (x, y)
    screen.blit(title, title_pos)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

white = (255, 255, 255)
black = (0, 0, 0)

run = True

pygame.init()
pygame.display.set_caption("EEG ADHD Neuro Feedback Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
while run:
    screen.fill(black)
    Show_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "Start!")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 애플리케이션을 종료하고자 하면
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    clock.tick(60)
    pygame.display.flip()

pygame.quit()