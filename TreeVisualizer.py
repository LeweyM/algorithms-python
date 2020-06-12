import random

import pygame
import sys

from RedBlackTree import RedBlackTree

HEIGHT = 600
WIDTH = 600

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
CENTER = (HALF_WIDTH, HALF_HEIGHT)

VERTICAL_SPACING = 100
RADIUS = 20


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
        left_position = (x - horizontal_spacing, (height+1)*vertical_spacing)
        pygame.draw.line(screen, WHITE, position, left_position, 2)
        draw_sub_tree(root.left, left_position, height + 1, vertical_spacing, screen)
    if root.right is not None:
        right_position = (x + horizontal_spacing, (height+1)*vertical_spacing)
        pygame.draw.line(screen, WHITE, position, right_position, 2)
        draw_sub_tree(root.right, right_position, height + 1, vertical_spacing, screen)
    draw_circle(screen, root, position)


def get_horizontal_spacing(height):
    split = 2 ** (height + 1)
    return WIDTH // split


def render(tree: RedBlackTree):
    pygame.init()

    size = WIDTH, HEIGHT
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        draw_tree(tree, screen)

        pygame.time.delay(1000)
        tree.put(random.randint(0, 100))

        pygame.display.flip()


def draw_circle(screen, node, position):
    pygame.draw.circle(screen, WHITE, position, RADIUS)
    text, text_rect = text_from_node(node.value, position)
    screen.blit(text, text_rect)


def text_from_node(value, position):
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(str(value), True, BLUE, None)
    text_rect = text.get_rect()
    text_rect.center = position
    return text, text_rect


if __name__ == '__main__':
    red_black_tree = RedBlackTree()
    render(red_black_tree)
