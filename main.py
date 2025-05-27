import pygame
import time 
pygame.init()
color_back = (87,3,89)
window = pygame.display.set_mode((500, 500))
window.fill(color_back)
#Создаём таймер
clock = pygame.time.Clock()

##класс для прямоугольной области
class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
        ##класс для надписи
class Label(Area):
    def set_text(self, text, fsize = 12, color_text = (0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, color_text)
    def draw(self, shift_x = 0, shift_y = 0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)   
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.set_text('click', 26)
    cards.append(new_card)
    x = x + 100
wait = 0
from random import randint
start_time = time.time()
cur_time = start_time
text1 = Label(0, 0, 50, 50, color_back)
text1.set_text('Время', 40, YELLOW)
text1.draw(20, 20)

timer = Label(50, 55, 50, 40, color_back)
timer.set_text('0', 40, YELLOW)
timer.draw(0, 0)

text1 = Label(380, 0, 50, 50, color_back)
text1.set_text('Счет', 45, YELLOW)
text1.draw(20, 20)

score = Label(430, 55, 50, 40, color_back)
score.set_text('0', 40, YELLOW)
score.draw(0, 0)
points = 0
while True:
    if wait == 0:
      #переносим надпись:
        wait = 20 #столько тиков надпись будет на одном месте
        click = randint(1, num_cards)
    for i in range(num_cards):
        cards[i].color((255,255,0))
        if (i + 1) == click:
            cards[i].draw(10, 40)
        else:
            cards[i].fill()
    else:
        wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].color(GREEN)
                        points += 1
                    else:
                        cards[i].color(RED)
                        points -= 1
                    cards[i].fill()
                    score.set_text(str(points), 40, YELLOW)
                    score.draw(0, 0)
    new_time = time.time()
    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, RED)
        win.set_text('Вы проиграли', 60, YELLOW)
        win.draw(110, 180)
        break
    pygame.display.update()
    clock.tick(40)
