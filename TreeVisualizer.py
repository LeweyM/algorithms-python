import random

import pygame
import sys

from RedBlackTree import RedBlackTree

RANDOM_UPPER_LIMIT = 100

DELAY_MILLISECONDS = 10

HEIGHT = 600
WIDTH = 1000

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

RED = pygame.Color("red")
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
CENTER = (HALF_WIDTH, HALF_HEIGHT)

VERTICAL_SPACING = 100
RADIUS = 15
FONT_SIZE = 10


def render(tree: RedBlackTree):
    pygame.init()

    size = WIDTH, HEIGHT
    black = 0, 0, 0
    key_counter = 0

    screen = pygame.display.set_mode(size)

    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.time.delay(DELAY_MILLISECONDS)
        tree.put(random.randint(0, RANDOM_UPPER_LIMIT))
        key_counter += 1

        draw_tree(tree, screen)
        write(screen, "Total Keys: " + str(key_counter), (WIDTH - 100, 20))

        pygame.display.flip()


def draw_tree(tree, screen):
    if tree.root is None:
        return
    vertical_spacing = HEIGHT // (tree.max_height() + 1)
    root_position = (HALF_WIDTH, vertical_spacing)
    draw_sub_tree(tree.root, root_position, 1, vertical_spacing, screen)


def draw_sub_tree(root, position, height, vertical_spacing, screen):
    horizontal_spacing = get_horizontal_spacing(height)
    x, y = position
    if root.left is not None:
        left_position = (x - horizontal_spacing, (height + 1) * vertical_spacing)
        draw_line(left_position, position, root.left.color, screen)
        draw_sub_tree(root.left, left_position, height + 1, vertical_spacing, screen)
    if root.right is not None:
        right_position = (x + horizontal_spacing, (height + 1) * vertical_spacing)
        draw_line(right_position, position, root.right.color, screen)
        draw_sub_tree(root.right, right_position, height + 1, vertical_spacing, screen)
    draw_circle(screen, root, position)


def get_horizontal_spacing(height):
    split = 2 ** (height + 1)
    return WIDTH // split


def draw_line(start, finish, color, screen):
    line_color = RED if color == 1 else WHITE
    pygame.draw.line(screen, line_color, finish, start, 2)


def draw_circle(screen, node, position):
    pygame.draw.circle(screen, WHITE, position, RADIUS)
    write(screen, str(node.value), position, BLUE)


def write(screen, text, position, color=WHITE):
    font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
    text = font.render(text, True, color, None)
    text_rect = text.get_rect()
    text_rect.center = position
    screen.blit(text, text_rect)


if __name__ == '__main__':
    red_black_tree = RedBlackTree()
    render(red_black_tree)
