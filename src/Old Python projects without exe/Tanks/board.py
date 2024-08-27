import pygame
import os


def load_image(name):
    fullname = os.path.join('tanks_sprites', name)
    image = pygame.image.load(fullname)
    return image


block = load_image("block.png")
block_2 = load_image("block_2.png")


class Board:
    def __init__(self, width, height, me, en_1, en_2, en_3):
        self.me = me
        self.en_1 = en_1
        self.en_2 = en_2
        self.en_3 = en_3
        self.width = width
        self.height = height
        self.left = 0
        self.top = 0
        self.cell_size = 40

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, "white", ((j * self.cell_size + self.left, i * self.cell_size + self.top),
                                                   (self.cell_size, self.cell_size)), 1)

    def render_2(self, screen, board_n):
        all_sprites = pygame.sprite.Group()
        for i in range(self.height):
            for j in range(self.width):
                if board_n[i][j] == 0:
                    n = pygame.sprite.Sprite()
                    n.image = block
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                elif board_n[i][j] == 1:
                    n = pygame.sprite.Sprite()
                    n.image = block_2
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                elif board_n[i][j] == 2:
                    n = self.me
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                elif board_n[i][j] == 3:
                    n = self.en_1
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                elif board_n[i][j] == 4:
                    n = self.en_2
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                elif board_n[i][j] == 5:
                    n = self.en_3
                    n.rect = n.image.get_rect()
                    all_sprites.add(n)
                    n.rect.x = j * self.cell_size + self.left
                    n.rect.y = i * self.cell_size + self.top
                all_sprites.draw(screen)

    def draw_words(self, screen, m, hp, l_n, dmg, acc, max_hp, cost_d, cost_h, cost_a, sc):
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = font.render(f"Урон: {dmg}", True, (255, 0, 0))
        text_x = 850
        text_y = 40
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 0, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 14)
        text = font.render(f"Нажмите Y, чтобы улучшить за {cost_d}", True, (117, 187, 253))
        text_x = 820
        text_y = 100
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (117, 187, 253), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Точность: {acc}%", True, (255, 0, 0))
        text_x = 813
        text_y = 160
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 0, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 14)
        text = font.render(f"Нажмите I, чтобы улучшить за {cost_a}", True, (117, 187, 253))
        text_x = 820
        text_y = 220
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (117, 187, 253), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Хп_макс: {max_hp}", True, (255, 0, 0))
        text_x = 823
        text_y = 280
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 0, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 14)
        text = font.render(f"Нажмите G, чтобы улучшить за {cost_h}", True, (117, 187, 253))
        text_x = 820
        text_y = 340
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (117, 187, 253), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Монет: {m}", True, (0, 255, 0))
        text_x = 830
        text_y = 400
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        text = font.render(f"Хп: {hp}", True, (0, 255, 0))
        text_x = 850
        text_y = 520
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        text = font.render(f"Уровень {l_n}", True, (255, 255, 255))
        text_x = 840
        text_y = 760
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
        text = font.render(f"Счет: {sc}", True, (255, 255, 255))
        text_x = 860
        text_y = 680
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)
