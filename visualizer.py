"""This module contains a visualizer for sorting algorithms
"""
import os
from collections import namedtuple

import pygame

from algorithms import Algorithms

WIDTH = int(1024 * 1.5)
HEIGHT = int(512 * 1.25)
Color = namedtuple("Color", ["r", "g", "b"])
WHITE = Color(255, 255, 255)
GREY = Color(160, 160, 160)
LIGHT_GREY = Color(210, 210, 210)
BLUE = Color(70, 219, 219)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
ICON = pygame.image.load(os.path.join(os.getcwd(), "assets", "img", "chart.jpg"))
pygame.display.set_icon(ICON)
display.fill(GREY)

BUT_WIDTH = 100
BUT_HEIGHT = 40
BUT_Y = HEIGHT - 70
REGEN_BUT_X = 60
SELECT_BUT_X = 250
INSERT_BUT_X = SELECT_BUT_X + 130 * 1
MERGE_BUT_X = SELECT_BUT_X + 130 * 2
QUICK_BUT_X = SELECT_BUT_X + 130 * 3
HEAP_BUT_X = SELECT_BUT_X + 130 * 4
regen_but = pygame.Rect(REGEN_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
select_but = pygame.Rect(SELECT_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
insert_but = pygame.Rect(INSERT_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
merge_but = pygame.Rect(MERGE_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
quick_but = pygame.Rect(QUICK_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
heap_but = pygame.Rect(HEAP_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)

SLIDE_X = QUICK_BUT_X + 500
SLIDE_WIDTH = 10
SLIDE_SPACING = 60
slide_bar = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_SPACING * 5 + 10, BUT_HEIGHT)
size_32 = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
size_64 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 1, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
size_128 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 2, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
size_256 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 3, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
size_512 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 4, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
size_1024 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 5, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
ARR_SIZE = 128

RUNNING = True


def draw_buttons():
    """Drawing the buttons for the pygame GUI
    """
    if regen_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, regen_but)
    else:
        pygame.draw.rect(display, WHITE, regen_but)
    if select_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, select_but)
    else:
        pygame.draw.rect(display, WHITE, select_but)
    if insert_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, insert_but)
    else:
        pygame.draw.rect(display, WHITE, insert_but)
    if merge_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, merge_but)
    else:
        pygame.draw.rect(display, WHITE, merge_but)
    if quick_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, quick_but)
    else:
        pygame.draw.rect(display, WHITE, quick_but)
    if heap_but.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(display, LIGHT_GREY, heap_but)
    else:
        pygame.draw.rect(display, WHITE, heap_but)

    pygame.draw.rect(display, WHITE, slide_bar)
    pygame.draw.rect(display, LIGHT_GREY, size_32)
    pygame.draw.rect(display, LIGHT_GREY, size_64)
    pygame.draw.rect(display, LIGHT_GREY, size_128)
    pygame.draw.rect(display, LIGHT_GREY, size_256)
    pygame.draw.rect(display, LIGHT_GREY, size_512)
    pygame.draw.rect(display, LIGHT_GREY, size_1024)
    if ARR_SIZE == 32:
        pygame.draw.rect(display, BLACK, size_32)
    elif ARR_SIZE == 64:
        pygame.draw.rect(display, BLACK, size_64)
    elif ARR_SIZE == 128:
        pygame.draw.rect(display, BLACK, size_128)
    elif ARR_SIZE == 256:
        pygame.draw.rect(display, BLACK, size_256)
    elif ARR_SIZE == 512:
        pygame.draw.rect(display, BLACK, size_512)
    elif ARR_SIZE == 1024:
        pygame.draw.rect(display, BLACK, size_1024)

    font = pygame.font.SysFont("calibri", 20)
    text = font.render("regenerate", True, BLACK)
    text_x = REGEN_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("selection", True, BLACK)
    text_x = SELECT_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("insertion", True, BLACK)
    text_x = INSERT_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("merge", True, BLACK)
    text_x = MERGE_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("quick", True, BLACK)
    text_x = QUICK_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("heap", True, BLACK)
    text_x = HEAP_BUT_X + (BUT_WIDTH - text.get_width()) // 2
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("small", True, BLACK)
    text_x = int(SLIDE_X - text.get_width() * 1.5)
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))

    text = font.render("big", True, BLACK)
    text_x = int(SLIDE_X + SLIDE_SPACING * 5 + 10 + text.get_width())
    text_y = BUT_Y + (BUT_HEIGHT - text.get_height()) // 2
    display.blit(text, (text_x, text_y))


def update_gui(
    arr, arr_size, one=None, two=None, three=None, done=False, sorting=False
):
    """Refresh the pygame GUI window

    Args:
        arr (list): the list that is being sorted
        arr_size (int): size of the list
        one (int, optional): index to be colored yellow. Defaults to None.
        two (int, optional): index to be colored yellow. Defaults to None.
        three (int, optional): index to be colored green. Defaults to None.
        done (bool, optional): True if sorting has finished, else False. Defaults to False.
        sorting (bool, optional): True if list is being sorted, else False. Defaults to False.
    """
    global RUNNING, ARR_SIZE
    ARR_SIZE = arr_size

    display.fill(GREY)

    draw_buttons()

    wid = 1024 / ARR_SIZE
    space = WIDTH / ARR_SIZE
    hei = 128 / ARR_SIZE
    for i, elem in enumerate(arr):
        if i in (one, two):
            color = YELLOW
        elif i == three:
            color = GREEN
        else:
            color = BLUE

        if done:
            color = GREEN
        pygame.draw.rect(display, color, (i * space, 0, wid, elem * hei))

    if sorting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break

    pygame.display.update()


def mouse_click(pos):
    """Detecting which button the user pressed

    Args:
        pos (tuple): pos[0] is the x coordinate, pos[1] is the y coordinate
    """
    global ARR_SIZE, algo

    if regen_but.collidepoint(pos):
        algo = Algorithms(ARR_SIZE, True)
    elif select_but.collidepoint(pos):
        algo.sorted = False
        algo.selection_sort()
    elif insert_but.collidepoint(pos):
        algo.sorted = False
        algo.insertion_sort()
    elif merge_but.collidepoint(pos):
        algo.sorted = False
        algo.merge_sort()
    elif quick_but.collidepoint(pos):
        algo.sorted = False
        algo.quick_sort()
    elif heap_but.collidepoint(pos):
        algo.sorted = False
        algo.heap_sort()
    elif size_32.collidepoint(pos):
        ARR_SIZE = 32
        algo = Algorithms(ARR_SIZE, True)
    elif size_64.collidepoint(pos):
        ARR_SIZE = 64
        algo = Algorithms(ARR_SIZE, True)
    elif size_128.collidepoint(pos):
        ARR_SIZE = 128
        algo = Algorithms(ARR_SIZE, True)
    elif size_256.collidepoint(pos):
        ARR_SIZE = 256
        algo = Algorithms(ARR_SIZE, True)
    elif size_512.collidepoint(pos):
        ARR_SIZE = 512
        algo = Algorithms(ARR_SIZE, True)
    elif size_1024.collidepoint(pos):
        ARR_SIZE = 1024
        algo = Algorithms(ARR_SIZE, True)


def main():
    """Main function of this module
    """
    global RUNNING, algo

    algo = Algorithms(ARR_SIZE, True)
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click(pygame.mouse.get_pos())

        if algo.sorted:
            update_gui(algo.array, ARR_SIZE, done=True)
        else:
            update_gui(algo.array, ARR_SIZE)
        pygame.display.update()


if __name__ == "__main__":
    main()
