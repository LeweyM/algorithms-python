import pygame
import sys

from RedBlackTree import RedBlackTree

HEIGHT = 600
WIDTH = 600

WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
CENTER = (WIDTH // 2, HEIGHT // 2)

RADIUS = 20


def render(tree: RedBlackTree):
    pygame.init()
    root = tree.root.value

    size = WIDTH, HEIGHT
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(str(root), True, BLUE, None)
    text_rect = text.get_rect()
    text_rect.center = CENTER

    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.circle(screen, WHITE, CENTER, RADIUS)
        screen.blit(text, text_rect)

        pygame.display.flip()


if __name__ == '__main__':
    red_black_tree = RedBlackTree()
    red_black_tree.put(5)
    render(red_black_tree)
