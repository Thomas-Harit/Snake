import pygame
import random

pygame.init()

class SnakeHead:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 20
        self.height = 20
        self.direction = 'up'

    def draw(self):
        pygame.draw.rect(window, DARK_GREEN, (self.x, self.y, self.length, self.height))

class SnakeTail:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.length = 20
        self.height = 20
        self.time = time

    def draw(self):
        pygame.draw.rect(window, LIGHT_GREEN, (self.x, self.y, self.length, self.height))

    def remove_self(self):
        tail_list_object.remove(self)

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 20
        self.height = 20

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, self.length, self.height))

    def spawnNewLocation(self):
        self.x = random.randint(0, window_length // 20) * 20
        self.y = random.randint(0, window_height // 20) * 20

class ScoreDisplay:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0

    def draw(self):
        text = font.render("{}".format(self.score), True, WHITE)
        window.blit(text, (self.x, self.y))

def reset_game():
    global tail_list_object, tail_length
    head.x = 100
    head.y = 100

    apple.spawnNewLocation()
    score_board.score = 0
    tail_list_object = []
    tail_length = 1

window_length = 700
window_height = 600

window = pygame.display.set_mode((window_length, window_height))
font = pygame.font.SysFont("comicsansms", 24)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)

head = SnakeHead(100, 100)
apple = Apple(160, 160)
score_board = ScoreDisplay(0, 0)

tail_length = 0
tail_list_object = []
die_from_tail = True


main = True

while main == True:

    pygame.time.delay(50)

    '''EVENT'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                head.direction = "up"
            elif event.key == pygame.K_DOWN:
                head.direction = "down"
            elif event.key == pygame.K_LEFT:
                head.direction = "left"
            elif event.key == pygame.K_RIGHT:
                head.direction = "right"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if die_from_tail == True:
                    die_from_tail = False
                else:
                    die_from_tail = True

    '''SNAKE EAT'''
    if head.x == apple.x and head.y == apple.y:
        apple.spawnNewLocation()
        tail_length += 1
        score_board.score += 1

    tail_list_object.append(SnakeTail(head.x, head.y, tail_length))

    '''SNAKE MOVE'''
    if head.direction == "up":
        head.y -= 20
    elif head.direction == "down":
        head.y += 20
    elif head.direction == "left":
        head.x -= 20
    elif head.direction == "right":
        head.x += 20

    '''SNAKE BORDER'''
    if head.x < 0:
        head.x = 0
    elif head.x + head.length > window_length:
        head.x = window_length - head.length
    if head.y < 0:
        head.y = 0
    elif head.y + head.height > window_height:
        head.y = window_height - head.height

    '''DRAW'''
    pygame.draw.rect(window, BLACK, (0, 0, window_length, window_height))
    for tail in tail_list_object:
        if tail.time == 0:
            tail.remove_self()
        elif tail.x == head.x and tail.y == head.y and die_from_tail == True:
            reset_game()
        else:
            tail.time -= 1
            tail.draw()
    head.draw()
    apple.draw()
    score_board.draw()
    pygame.display.update()

pygame.quit()