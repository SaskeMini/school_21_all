import pygame
from board import Board
import os
from random import randint


def load_image(name):
    fullname = os.path.join('tanks_sprites', name)
    image = pygame.image.load(fullname)
    return image


def score_list(score_n):
    f3 = open("score.txt", "r")
    f2_read = f3.readlines()
    f2_list = []
    f2 = open("score.txt", "w")
    for g in f2_read:
        f2_list.append(int(g))
    f2_list.append(score_n)
    for g in sorted(f2_list, reverse=True):
        print(g, file=f2)


running = True
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
monet_number = 0
cost_dmg = 3
cost_hp = 3
cost_acc = 3
me_dmg = 3
hp_max = 15
me_acc = 75
l_n = 1
score = 0
f1 = open("level1.txt", "r")
char_pers = {}
me = pygame.sprite.Sprite()
life_en_1 = True
life_en_2 = True
life_en_3 = True
en_1 = pygame.sprite.Sprite()
en_2 = pygame.sprite.Sprite()
en_3 = pygame.sprite.Sprite()
me.image = load_image("tank_pl.png")
en_1.image = load_image("tank_en.png")
en_2.image = load_image("tank_en.png")
en_3.image = load_image("tank_en.png")
reading_lvl = f1.readlines()
board = Board(20, 20, me, en_1, en_2, en_3)
board_1 = []
for i in reading_lvl:
    a = []
    b = i.split()
    for j in b:
        a.append(int(j))
    board_1.append(a)
x_p, y_p = 0, 0
en_1_x, en_1_y = 0, 0
en_2_x, en_2_y = 0, 0
en_3_x, en_3_y = 0, 0
for i in board_1:
    for j in i:
        if j == 2:
            x_p, y_p = board_1.index(i), i.index(j)
        elif j == 3:
            en_1_x, en_1_y = board_1.index(i), i.index(j)
        elif j == 4:
            en_2_x, en_2_y = board_1.index(i), i.index(j)
        elif j == 5:
            en_3_x, en_3_y = board_1.index(i), i.index(j)
nap = ["left", "right", "up", "down"]
nap_now = "up"
nap_now_en_1 = "up"
nap_now_en_2 = "up"
nap_now_en_3 = "up"
en_move = False
en_attack_n = 0
all_sprites_4 = pygame.sprite.Group()
game = pygame.sprite.Sprite()
game.image = load_image("start.png")
game.rect = game.image.get_rect()
all_sprites_4.add(game)
game.rect.x = -800
game.rect.y = 0
while game.rect.x != 0:
    game.rect.x += 20
    all_sprites_4.draw(screen)
    pygame.display.flip()
    clock.tick(10)



def level_1():
    global f1
    global char_pers
    global hp_max
    global en_1, en_2, en_3
    global l_n
    global life_en_1, life_en_3, life_en_2
    global board
    global x_p, y_p, en_1_x, en_1_y, en_2_x, en_2_y, en_3_x, en_3_y
    global nap_now_en_1, nap_now_en_2, nap_now_en_3, nap, nap_now, en_move, en_attack_n
    global monet_number
    global board_1
    global cost_dmg, cost_hp, cost_acc, me_dmg, me_acc
    global score
    score = 0
    monet_number = 0
    cost_dmg = 3
    cost_hp = 3
    cost_acc = 3
    me_dmg = 3
    hp_max = 15
    me_acc = 75
    nap_now = "up"
    nap_now_en_1 = "up"
    nap_now_en_2 = "up"
    nap_now_en_3 = "up"
    en_move = False
    en_attack_n = 0
    f1 = open("level1.txt", "r")
    monet_number = 0
    char_pers = {"me": {"hp": hp_max, "dmg": me_dmg, "acc": me_acc}, "en_1": {"hp": 10, "dmg": 3, "acc": 50},
                 "en_2": {"hp": 10, "dmg": 3, "acc": 50}, "en_3": {"hp": 15, "dmg": 5, "acc": 65}}
    life_en_1 = True
    life_en_2 = True
    life_en_3 = True
    me.image = load_image("tank_pl.png")
    en_1.image = load_image("tank_en.png")
    en_2.image = load_image("tank_en.png")
    en_3.image = load_image("tank_en.png")
    l_n = 1
    board_1 = []
    reading_lvl = f1.readlines()
    for i in reading_lvl:
        a = []
        b = i.split()
        for j in b:
            a.append(int(j))
        board_1.append(a)
    x_p, y_p = 0, 0
    en_1_x, en_1_y = 0, 0
    en_2_x, en_2_y = 0, 0
    en_3_x, en_3_y = 0, 0
    for i in board_1:
        for j in i:
            if j == 2:
                x_p, y_p = board_1.index(i), i.index(j)
            elif j == 3:
                en_1_x, en_1_y = board_1.index(i), i.index(j)
            elif j == 4:
                en_2_x, en_2_y = board_1.index(i), i.index(j)
            elif j == 5:
                en_3_x, en_3_y = board_1.index(i), i.index(j)
    nap = ["left", "right", "up", "down"]
    board = Board(20, 20, me, en_1, en_2, en_3)


def level_2():
    global f1
    global char_pers
    global hp_max
    global en_1, en_2, en_3
    global l_n
    global life_en_1, life_en_3, life_en_2
    global board
    global x_p, y_p, en_1_x, en_1_y, en_2_x, en_2_y, en_3_x, en_3_y
    global nap_now_en_1, nap_now_en_2, nap_now_en_3, nap, nap_now, en_move, en_attack_n
    global board_1
    nap_now = "up"
    nap_now_en_1 = "up"
    nap_now_en_2 = "up"
    nap_now_en_3 = "up"
    en_move = False
    en_attack_n = 0
    f1 = open("level_2.txt", "r")
    char_pers = {"me": {"hp": hp_max, "dmg": me_dmg, "acc": me_acc}, "en_1": {"hp": 15, "dmg": 5, "acc": 65},
                 "en_2": {"hp": 15, "dmg": 5, "acc": 65}, "en_3": {"hp": 20, "dmg": 7, "acc": 80}}
    life_en_1 = True
    life_en_2 = True
    life_en_3 = True
    me.image = load_image("tank_pl.png")
    en_1.image = load_image("tank_en.png")
    en_2.image = load_image("tank_en.png")
    en_3.image = load_image("tank_en.png")
    l_n = 2
    board_1 = []
    reading_lvl = f1.readlines()
    board = Board(20, 20, me, en_1, en_2, en_3)
    for i in reading_lvl:
        a = []
        b = i.split()
        for j in b:
            a.append(int(j))
        board_1.append(a)
    x_p, y_p = 0, 0
    en_1_x, en_1_y = 0, 0
    en_2_x, en_2_y = 0, 0
    en_3_x, en_3_y = 0, 0
    for i in board_1:
        for j in i:
            if j == 2:
                x_p, y_p = board_1.index(i), i.index(j)
            elif j == 3:
                en_1_x, en_1_y = board_1.index(i), i.index(j)
            elif j == 4:
                en_2_x, en_2_y = board_1.index(i), i.index(j)
            elif j == 5:
                en_3_x, en_3_y = board_1.index(i), i.index(j)
    nap = ["left", "right", "up", "down"]


def level_3():
    global f1
    global char_pers
    global hp_max
    global en_1, en_2, en_3
    global l_n
    global life_en_1, life_en_3, life_en_2
    global board
    global x_p, y_p, en_1_x, en_1_y, en_2_x, en_2_y, en_3_x, en_3_y
    global nap_now_en_1, nap_now_en_2, nap_now_en_3, nap, nap_now, en_move, en_attack_n
    global board_1
    nap_now = "up"
    nap_now_en_1 = "up"
    nap_now_en_2 = "up"
    nap_now_en_3 = "up"
    en_move = False
    en_attack_n = 0
    f1 = open("level_3.txt", "r")
    char_pers = {"me": {"hp": hp_max, "dmg": me_dmg, "acc": me_acc}, "en_1": {"hp": 20, "dmg": 7, "acc": 80},
                 "en_2": {"hp": 20, "dmg": 7, "acc": 80}, "en_3": {"hp": 20, "dmg": 7, "acc": 80}}
    life_en_1 = True
    life_en_2 = True
    life_en_3 = True
    board_1 = []
    me.image = load_image("tank_pl.png")
    en_1.image = load_image("tank_en.png")
    en_2.image = load_image("tank_en.png")
    en_3.image = load_image("tank_en.png")
    l_n = 3
    reading_lvl = f1.readlines()
    board = Board(20, 20, me, en_1, en_2, en_3)
    for i in reading_lvl:
        a = []
        b = i.split()
        for j in b:
            a.append(int(j))
        board_1.append(a)
    x_p, y_p = 0, 0
    en_1_x, en_1_y = 0, 0
    en_2_x, en_2_y = 0, 0
    en_3_x, en_3_y = 0, 0
    for i in board_1:
        for j in i:
            if j == 2:
                x_p, y_p = board_1.index(i), i.index(j)
            elif j == 3:
                en_1_x, en_1_y = board_1.index(i), i.index(j)
            elif j == 4:
                en_2_x, en_2_y = board_1.index(i), i.index(j)
            elif j == 5:
                en_3_x, en_3_y = board_1.index(i), i.index(j)
    nap = ["left", "right", "up", "down"]


if l_n == 1:
    level_1()
elif l_n == 2:
    level_2()
elif l_n == 3:
    level_3()
all_sprites_2 = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites_2)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for y in range(rows):
            for x in range(columns):
                frame_location = (self.rect.w * x, self.rect.h * y)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


monet = AnimatedSprite(load_image("monet.png"), 6, 1, 944, 392)
heard = AnimatedSprite(load_image("heard.png"), 1, 1, 944, 508)


def enemy_pov(en_x, en_y, nap_now_en, en_im):
    global x_p
    global y_p
    nap_new = ""
    if x_p > en_x:
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, 90)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, -90)
        nap_new = "down"
    elif x_p < en_x:
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, -90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, 90)
        nap_new = "up"
    elif y_p > en_y:
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, -90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, 90)
        nap_new = "right"
    elif y_p < en_y:
        if nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, 90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, -90)
        nap_new = "left"
    return nap_new, en_im


def enemy_attack(x_p_e, y_p_e, nap_now_e, n_e):
    global char_pers
    coord_bom_e = []
    check_attack = False
    if nap_now_e == "right":
        if y_p_e <= 17:
            if board_1[x_p_e][y_p_e + 1] != 1 and board_1[x_p_e][y_p_e + 2] != 1:
                coord_bom_e = [(y_p_e * 40 + 40, x_p_e * 40 + 19), (y_p_e * 40 + 120, x_p_e * 40 + 19)]
                if board_1[x_p_e][y_p_e + 1] == 2 or board_1[x_p_e][y_p_e + 2] == 2:
                    check_attack = True
        elif y_p_e == 18 or board_1[x_p_e][y_p_e + 2] == 1:
            coord_bom_e = [(y_p_e * 40 + 40, x_p_e * 40 + 19), (y_p_e * 40 + 80, x_p_e * 40 + 19)]
            if board_1[x_p_e][y_p_e + 1] == 2:
                check_attack = True
    elif nap_now_e == "left":
        if y_p_e >= 1:
            if board_1[x_p_e][y_p_e - 1] != 1 and board_1[x_p_e][y_p_e - 2] != 1:
                coord_bom_e = [(y_p_e * 40, x_p_e * 40 + 19), (y_p_e * 40 - 80, x_p_e * 40 + 19)]
                if board_1[x_p_e][y_p_e - 1] == 2 or board_1[x_p_e][y_p_e - 2] == 2:
                    check_attack = True
        elif y_p_e == 1 or board_1[x_p_e][y_p_e - 2] == 1:
            coord_bom_e = [(y_p_e * 40 + 40, x_p_e * 40 + 19), (y_p_e * 40 + 80, x_p_e * 40 + 19)]
            if board_1[x_p_e][y_p_e - 1] == 2:
                check_attack = True
    elif nap_now_e == "up":
        if board_1[x_p_e - 1][y_p_e] != 1 and board_1[x_p_e - 2][y_p_e] != 1:
            coord_bom_e = [(y_p_e * 40 + 19, x_p_e * 40), (y_p_e * 40 + 19, x_p_e * 40 - 80)]
            if board_1[x_p_e - 1][y_p_e] == 2 or board_1[x_p_e - 2][y_p_e] == 2:
                check_attack = True
        elif board_1[x_p_e - 2][y_p_e] == 1:
            coord_bom_e = [(y_p_e * 40 + 19, x_p_e * 40), (y_p_e * 40 + 19, x_p_e * 40 - 40)]
            if board_1[x_p_e - 1][y_p_e] == 2:
                check_attack = True
    elif nap_now_e == "down":
        if x_p_e <= 17:
            if board_1[x_p_e + 1][y_p_e] != 1 and board_1[x_p_e + 2][y_p_e] != 1 and x_p_e <= 17:
                coord_bom_e = [(y_p_e * 40 + 19, x_p_e * 40 + 40), (y_p_e * 40 + 19, x_p_e * 40 + 120)]
                if board_1[x_p_e + 1][y_p_e] == 2 or board_1[x_p_e + 2][y_p_e] == 2:
                    check_attack = True
        elif x_p_e == 18:
            coord_bom_e = [(y_p_e * 40 + 19, x_p_e * 40 + 40), (y_p_e * 40 + 19, x_p_e * 40 + 80)]
            if board_1[x_p_e + 1][y_p_e] == 2:
                check_attack = True
        elif x_p_e != 19:
            if board_1[x_p_e + 2][y_p_e] == 1:
                coord_bom_e = [(y_p_e * 40 + 19, x_p_e * 40 + 40), (y_p_e * 40 + 19, x_p_e * 40 + 80)]
                if board_1[x_p_e + 1][y_p_e] == 2:
                    check_attack = True
    if check_attack:
        if n_e == 1:
            if randint(0, 100) < char_pers["en_1"]["acc"] + 1:
                char_pers["me"]["hp"] -= char_pers["en_1"]["dmg"]
        elif n_e == 2:
            if randint(0, 100) < char_pers["en_2"]["acc"] + 1:
                char_pers["me"]["hp"] -= char_pers["en_2"]["dmg"]
        elif n_e == 3:
            if randint(0, 100) < char_pers["en_3"]["acc"] + 1:
                char_pers["me"]["hp"] -= char_pers["en_3"]["dmg"]
    return coord_bom_e


def enemy_move(en_m, en_x, en_y, nap_now_en, en_im, board_1):
    global x_p
    global y_p
    nap_new = ""
    if en_m == 0:
        if en_y - 1 >= 0:
            if board_1[en_x][en_y - 1] != 1 and board_1[en_x][en_y - 1] != 3 and \
                    board_1[en_x][en_y - 1] != 4 and board_1[en_x][en_y - 1] != 5 and \
                    board_1[en_x][en_y - 1] != board_1[x_p][y_p]:
                board_1[en_x][en_y - 1], board_1[en_x][en_y] = board_1[en_x][en_y], board_1[en_x][en_y - 1]
                en_y = en_y - 1
        if nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, 90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, -90)
        nap_new = "left"
    elif en_m == 1:
        if en_y + 1 <= 19:
            if board_1[en_x][en_y + 1] != 1 and board_1[en_x][en_y + 1] != 3 and \
                    board_1[en_x][en_y + 1] != 4 and board_1[en_x][en_y + 1] != 5 and \
                    board_1[en_x][en_y + 1] != 2:
                board_1[en_x][en_y + 1], board_1[en_x][en_y] = board_1[en_x][en_y], board_1[en_x][en_y + 1]
                en_y = en_y + 1
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, -90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, 90)
        nap_new = "right"
    elif en_m == 2:
        if en_x - 1 >= 0:
            if board_1[en_x - 1][en_y] != 1 and board_1[en_x - 1][en_y] != 3 and \
                    board_1[en_x - 1][en_y] != 4 and board_1[en_x - 1][en_y] != 5 and \
                    board_1[en_x - 1][en_y] != board_1[x_p][y_p]:
                board_1[en_x - 1][en_y], board_1[en_x][en_y] = board_1[en_x][en_y], board_1[en_x - 1][en_y]
                en_x = en_x - 1
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, -90)
        elif nap_now_en == "down":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, 90)
        nap_new = "up"
    elif en_m == 3:
        if en_x + 1 <= 19:
            if board_1[en_x + 1][en_y] != 1 and board_1[en_x + 1][en_y] != 3 and \
                    board_1[en_x + 1][en_y] != 4 and board_1[en_x + 1][en_y] != 5 and \
                    board_1[en_x + 1][en_y] != board_1[x_p][y_p]:
                board_1[en_x + 1][en_y], board_1[en_x][en_y] = board_1[en_x][en_y], board_1[en_x + 1][en_y]
                en_x = en_x + 1
        if nap_now_en == "left":
            en_im = pygame.transform.rotate(en_im, 90)
        elif nap_now_en == "up":
            en_im = pygame.transform.rotate(en_im, 180)
        elif nap_now_en == "right":
            en_im = pygame.transform.rotate(en_im, -90)
        nap_new = "down"
    return en_x, en_y, nap_new, en_im, board_1


coord_bom = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score_list(score)
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if nap_now == "right":
                    if y_p <= 17:
                        if board_1[x_p][y_p + 1] != 1 and board_1[x_p][y_p + 2] != 1:
                            coord_bom = [(y_p * 40 + 40, x_p * 40 + 19), (y_p * 40 + 120, x_p * 40 + 19)]
                            if board_1[x_p][y_p + 1] == 3 or board_1[x_p][y_p + 2] == 3:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 3
                            elif board_1[x_p][y_p + 1] == 4 or board_1[x_p][y_p + 2] == 4:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 4
                            elif board_1[x_p][y_p + 1] == 5 or board_1[x_p][y_p + 2] == 5:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 5
                    elif y_p == 18 or board_1[x_p][y_p + 2] == 1:
                        coord_bom = [(y_p * 40 + 40, x_p * 40 + 19), (y_p * 40 + 80, x_p * 40 + 19)]
                        if board_1[x_p][y_p + 1] == 3:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 3
                        elif board_1[x_p][y_p + 1] == 4:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 4
                        elif board_1[x_p][y_p + 1] == 5:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 5
                elif nap_now == "left":
                    if y_p >= 1:
                        if board_1[x_p][y_p - 1] != 1 and board_1[x_p][y_p - 2] != 1:
                            coord_bom = [(y_p * 40, x_p * 40 + 19), (y_p * 40 - 80, x_p * 40 + 19)]
                            if board_1[x_p][y_p - 1] == 3 or board_1[x_p][y_p - 2] == 3:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 3
                            elif board_1[x_p][y_p - 1] == 4 or board_1[x_p][y_p - 2] == 4:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 4
                            elif board_1[x_p][y_p - 1] == 5 or board_1[x_p][y_p - 2] == 5:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 5
                    elif y_p == 1 or board_1[x_p][y_p - 2] == 1:
                        coord_bom = [(y_p * 40 + 40, x_p * 40 + 19), (y_p * 40 + 80, x_p * 40 + 19)]
                        if board_1[x_p][y_p - 1] == 3:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 3
                        elif board_1[x_p][y_p - 1] == 4:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 4
                        elif board_1[x_p][y_p - 1] == 5:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 5
                elif nap_now == "up":
                    if board_1[x_p - 1][y_p] != 1 and board_1[x_p - 2][y_p] != 1:
                        coord_bom = [(y_p * 40 + 19, x_p * 40), (y_p * 40 + 19, x_p * 40 - 80)]
                        if board_1[x_p - 1][y_p] == 3 or board_1[x_p - 2][y_p] == 3:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 3
                        elif board_1[x_p - 1][y_p] == 4 or board_1[x_p - 2][y_p] == 4:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 4
                        elif board_1[x_p - 1][y_p] == 5 or board_1[x_p - 2][y_p] == 5:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 5
                    elif board_1[x_p - 2][y_p] == 1:
                        coord_bom = [(y_p * 40 + 19, x_p * 40), (y_p * 40 + 19, x_p * 40 - 40)]
                        if board_1[x_p - 1][y_p] == 3:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 3
                        elif board_1[x_p - 1][y_p] == 4:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 4
                        elif board_1[x_p - 1][y_p] == 5:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 5
                elif nap_now == "down":
                    if x_p <= 17:
                        if board_1[x_p + 1][y_p] != 1 and board_1[x_p + 2][y_p] != 1 and x_p <= 17:
                            coord_bom = [(y_p * 40 + 19, x_p * 40 + 40), (y_p * 40 + 19, x_p * 40 + 120)]
                            if board_1[x_p + 1][y_p] == 3 or board_1[x_p + 2][y_p] == 3:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 3
                            elif board_1[x_p + 1][y_p] == 4 or board_1[x_p + 2][y_p] == 4:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 4
                            elif board_1[x_p + 1][y_p] == 5 or board_1[x_p + 2][y_p] == 5:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 5
                    elif x_p == 18:
                        coord_bom = [(y_p * 40 + 19, x_p * 40 + 40), (y_p * 40 + 19, x_p * 40 + 80)]
                        if board_1[x_p + 1][y_p] == 3:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 3
                        elif board_1[x_p + 1][y_p] == 4:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 4
                        elif board_1[x_p + 1][y_p] == 5:
                            if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                            en_attack_n = 5
                    elif x_p != 19:
                        if board_1[x_p + 2][y_p] == 1:
                            coord_bom = [(y_p * 40 + 19, x_p * 40 + 40), (y_p * 40 + 19, x_p * 40 + 80)]
                            if board_1[x_p + 1][y_p] == 3:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_1"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 3
                            elif board_1[x_p + 1][y_p] == 4:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_2"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 4
                            elif board_1[x_p + 1][y_p] == 5:
                                if randint(0, 100) < char_pers["me"]["acc"] + 1:
                                    char_pers["en_3"]["hp"] -= char_pers["me"]["dmg"]
                                en_attack_n = 5
            elif event.key == pygame.K_LEFT:
                if y_p - 1 >= 0:
                    if board_1[x_p][y_p - 1] != 1 and board_1[x_p][y_p - 1] != 3 and \
                            board_1[x_p][y_p - 1] != 4 and board_1[x_p][y_p - 1] != 5:
                        board_1[x_p][y_p - 1], board_1[x_p][y_p] = board_1[x_p][y_p], board_1[x_p][y_p - 1]
                        y_p = y_p - 1
                        en_move = True
                    if nap_now == "right":
                        me.image = pygame.transform.rotate(me.image, 180)
                    elif nap_now == "up":
                        me.image = pygame.transform.rotate(me.image, 90)
                    elif nap_now == "down":
                        me.image = pygame.transform.rotate(me.image, -90)
                    nap_now = "left"
            elif event.key == pygame.K_RIGHT:
                if y_p + 1 <= 19:
                    if board_1[x_p][y_p + 1] != 1 and board_1[x_p][y_p + 1] != 3 and \
                            board_1[x_p][y_p + 1] != 4 and board_1[x_p][y_p + 1] != 5:
                        board_1[x_p][y_p + 1], board_1[x_p][y_p] = board_1[x_p][y_p], board_1[x_p][y_p + 1]
                        y_p = y_p + 1
                        en_move = True
                    if nap_now == "left":
                        me.image = pygame.transform.rotate(me.image, -180)
                    elif nap_now == "up":
                        me.image = pygame.transform.rotate(me.image, -90)
                    elif nap_now == "down":
                        me.image = pygame.transform.rotate(me.image, 90)
                    nap_now = "right"
            elif event.key == pygame.K_UP:
                if x_p - 1 >= 0:
                    if board_1[x_p - 1][y_p] != 1 and board_1[x_p - 1][y_p] != 3 and \
                            board_1[x_p - 1][y_p] != 4 and board_1[x_p - 1][y_p] != 5:
                        board_1[x_p - 1][y_p], board_1[x_p][y_p] = board_1[x_p][y_p], board_1[x_p - 1][y_p]
                        x_p = x_p - 1
                        en_move = True
                    if nap_now == "left":
                        me.image = pygame.transform.rotate(me.image, -90)
                    elif nap_now == "down":
                        me.image = pygame.transform.rotate(me.image, 180)
                    elif nap_now == "right":
                        me.image = pygame.transform.rotate(me.image, 90)
                    nap_now = "up"
            elif event.key == pygame.K_DOWN:
                if x_p + 1 <= 19:
                    if board_1[x_p + 1][y_p] != 1 and board_1[x_p + 1][y_p] != 3 and \
                            board_1[x_p + 1][y_p] != 4 and board_1[x_p + 1][y_p] != 5:
                        board_1[x_p + 1][y_p], board_1[x_p][y_p] = board_1[x_p][y_p], board_1[x_p + 1][y_p]
                        x_p = x_p + 1
                        en_move = True
                    if nap_now == "left":
                        me.image = pygame.transform.rotate(me.image, 90)
                    elif nap_now == "up":
                        me.image = pygame.transform.rotate(me.image, 180)
                    elif nap_now == "right":
                        me.image = pygame.transform.rotate(me.image, -90)
                    nap_now = "down"
            elif event.key == pygame.K_s:
                if nap_now == "left":
                    me.image = pygame.transform.rotate(me.image, 90)
                elif nap_now == "up":
                    me.image = pygame.transform.rotate(me.image, 180)
                elif nap_now == "right":
                    me.image = pygame.transform.rotate(me.image, -90)
                nap_now = "down"
            elif event.key == pygame.K_w:
                if nap_now == "left":
                    me.image = pygame.transform.rotate(me.image, -90)
                elif nap_now == "down":
                    me.image = pygame.transform.rotate(me.image, 180)
                elif nap_now == "right":
                    me.image = pygame.transform.rotate(me.image, 90)
                nap_now = "up"
            elif event.key == pygame.K_d:
                if nap_now == "left":
                    me.image = pygame.transform.rotate(me.image, -180)
                elif nap_now == "up":
                    me.image = pygame.transform.rotate(me.image, -90)
                elif nap_now == "down":
                    me.image = pygame.transform.rotate(me.image, 90)
                nap_now = "right"
            elif event.key == pygame.K_a:
                if nap_now == "right":
                    me.image = pygame.transform.rotate(me.image, 180)
                elif nap_now == "up":
                    me.image = pygame.transform.rotate(me.image, 90)
                elif nap_now == "down":
                    me.image = pygame.transform.rotate(me.image, -90)
                nap_now = "left"
            elif event.key == pygame.K_y:
                if monet_number >= cost_dmg:
                    monet_number -= cost_dmg
                    cost_dmg += 2
                    me_dmg += 2
            elif event.key == pygame.K_i:
                if monet_number >= cost_acc:
                    monet_number -= cost_acc
                    cost_acc += 2
                    me_acc += 5
            elif event.key == pygame.K_g:
                if monet_number >= cost_hp:
                    monet_number -= cost_hp
                    cost_hp += 2
                    hp_max += 3
                    char_pers["me"]["hp"] = hp_max
            score += 1
    screen.fill((0, 0, 0))
    board = Board(20, 20, me, en_1, en_2, en_3)
    board.render(screen)
    board.render_2(screen, board_1)
    board.draw_words(screen, monet_number, char_pers["me"]["hp"], l_n, me_dmg, me_acc, hp_max, cost_dmg,
                     cost_hp, cost_acc, score)
    if en_move:
        if life_en_1:
            en_m_1 = randint(0, 3)
            en_1_x, en_1_y, nap_now_en_1, en_1.image, board_1 = enemy_move(en_m_1, en_1_x, en_1_y,
                                                                           nap_now_en_1, en_1.image, board_1)
        if life_en_2:
            en_m_2 = randint(0, 3)
            en_2_x, en_2_y, nap_now_en_2, en_2.image, board_1 = enemy_move(en_m_2, en_2_x, en_2_y,
                                                                           nap_now_en_2, en_2.image, board_1)
        if life_en_3:
            en_m_3 = randint(0, 3)
            en_3_x, en_3_y, nap_now_en_3, en_3.image, board_1 = enemy_move(en_m_3, en_3_x, en_3_y,
                                                                           nap_now_en_3, en_3.image, board_1)
        en_move = False
    elif en_attack_n != 0:
        if en_attack_n == 3:
            if life_en_1:
                nap_now_en_1, en_1.image = enemy_pov(en_1_x, en_1_y, nap_now_en_1, en_1.image)
                coord_bom_en = enemy_attack(en_1_x, en_1_y, nap_now_en_1, 1)
                pygame.draw.line(screen, (255, 0, 255), coord_bom_en[0], coord_bom_en[1], 3)
        elif en_attack_n == 4:
            if life_en_2:
                nap_now_en_2, en_2.image = enemy_pov(en_2_x, en_2_y, nap_now_en_2, en_2.image)
                coord_bom_en = enemy_attack(en_2_x, en_2_y, nap_now_en_2, 2)
                pygame.draw.line(screen, (255, 0, 255), coord_bom_en[0], coord_bom_en[1], 3)
        elif en_attack_n == 5:
            if life_en_3:
                nap_now_en_3, en_3.image = enemy_pov(en_3_x, en_3_y, nap_now_en_3, en_3.image)
                coord_bom_en = enemy_attack(en_3_x, en_3_y, nap_now_en_3, 3)
                pygame.draw.line(screen, (255, 0, 255), coord_bom_en[0], coord_bom_en[1], 3)
        en_attack_n = 0
    if coord_bom:
        pygame.draw.line(screen, (0, 255, 0), coord_bom[0], coord_bom[1], 3)
        coord_bom = []
    s_1 = False
    s_2 = False
    s_3 = False
    if char_pers["en_1"]["hp"] <= 0 and life_en_1:
        life_en_1 = False
        en_1.image = load_image("tank_die.png")
        if nap_now_en_1 == "right":
            en_1.image = pygame.transform.rotate(en_1.image, -90)
        elif nap_now_en_1 == "left":
            en_1.image = pygame.transform.rotate(en_1.image, 90)
        elif nap_now_en_1 == "down":
            en_1.image = pygame.transform.rotate(en_1.image, 180)
        s_1 = True
        score += 3 * l_n
    if char_pers["en_2"]["hp"] <= 0 and life_en_2:
        life_en_2 = False
        en_2.image = load_image("tank_die.png")
        if nap_now_en_2 == "right":
            en_2.image = pygame.transform.rotate(en_2.image, -90)
        elif nap_now_en_2 == "left":
            en_2.image = pygame.transform.rotate(en_2.image, 90)
        elif nap_now_en_2 == "down":
            en_2.image = pygame.transform.rotate(en_2.image, 180)
        s_2 = True
        score += 6 * l_n
    if char_pers["en_3"]["hp"] <= 0 and life_en_3:
        life_en_3 = False
        en_3.image = load_image("tank_die.png")
        if nap_now_en_3 == "right":
            en_3.image = pygame.transform.rotate(en_3.image, -90)
        elif nap_now_en_3 == "left":
            en_3.image = pygame.transform.rotate(en_3.image, 90)
        elif nap_now_en_3 == "down":
            en_3.image = pygame.transform.rotate(en_3.image, 180)
        s_3 = True
        score += 9 * l_n
    if s_1:
        monet_number += 6 * l_n
    if s_2:
        monet_number += 6 * l_n
    if s_3:
        monet_number += 9 * l_n
    if char_pers["me"]["hp"] <= 0:
        score_list(score)
        screen.fill((0, 0, 0))
        board = Board(20, 20, me, en_1, en_2, en_3)
        board.render(screen)
        board.render_2(screen, board_1)
        board.draw_words(screen, monet_number, char_pers["me"]["hp"], l_n, me_dmg, me_acc, hp_max, cost_dmg,
                         cost_hp, cost_acc, score)
        all_sprites_4 = pygame.sprite.Group()
        game = pygame.sprite.Sprite()
        game.image = load_image("gameover.png")
        game.rect = game.image.get_rect()
        all_sprites_4.add(game)
        game.rect.x = -800
        game.rect.y = 0
        while game.rect.x != 0:
            game.rect.x += 20
            all_sprites_4.draw(screen)
            pygame.display.flip()
            clock.tick(10)
        level_1()
    if not life_en_1 and not life_en_2 and not life_en_3 and char_pers["me"]["hp"] > 0:
        if l_n == 1:
            l_n = 2
            level_2()
        elif l_n == 2:
            l_n = 3
            level_3()
        elif l_n == 3:
            running = False
    all_sprites_2.draw(screen)
    all_sprites_2.update()
    pygame.display.flip()
