"""This module contains a visualizer class for 5 pathfinding algorithms
"""
import os
import sys
from collections import namedtuple

import pygame

from algorithms import Algorithms

Color = namedtuple("Color", ["r", "g", "b"])
WHITE = Color(255, 255, 255)
GREY = Color(160, 160, 160)
LIGHT_GREY = Color(210, 210, 210)
BLUE = Color(80, 230, 230)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)


class AlgoVisualizer(Algorithms):
    """This class contains a visualizer for my implementation
    of common sorting algorithms
    """

    WIDTH = int(1024 * 1.5)
    HEIGHT = int(512 * 1.25)

    BUT_WIDTH = 100
    BUT_HEIGHT = 40
    BUT_Y = HEIGHT - 70
    REGEN_BUT_X = 60
    SELECT_BUT_X = 250
    INSERT_BUT_X = SELECT_BUT_X + 130 * 1
    MERGE_BUT_X = SELECT_BUT_X + 130 * 2
    QUICK_BUT_X = SELECT_BUT_X + 130 * 3
    HEAP_BUT_X = SELECT_BUT_X + 130 * 4
    SLIDE_X = QUICK_BUT_X + 500
    SLIDE_WIDTH = 10
    SLIDE_SPACING = 60

    regen_but = pygame.Rect(REGEN_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    select_but = pygame.Rect(SELECT_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    insert_but = pygame.Rect(INSERT_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    merge_but = pygame.Rect(MERGE_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    quick_but = pygame.Rect(QUICK_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    heap_but = pygame.Rect(HEAP_BUT_X, BUT_Y, BUT_WIDTH, BUT_HEIGHT)
    but_list = [regen_but, select_but, insert_but, merge_but, quick_but, heap_but]
    but_order = ["regenerate", "selection", "insertion", "merge", "quick", "heap"]

    slide_bar = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_SPACING * 5 + 10, BUT_HEIGHT)
    size_32 = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_64 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 1, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_128 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 2, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_256 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 3, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_512 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 4, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_1024 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 5, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    tick_list = [size_32, size_64, size_128, size_256, size_512, size_1024]
    tick_size = [32, 64, 128, 256, 512, 1024]

    ICON = pygame.image.load(os.path.join(os.getcwd(), "assets", "img", "chart.jpg"))

    def __init__(self):
        super().__init__(128, True)
        self.sort_dict = {
            "selection": self.selection_sort,
            "insertion": self.insertion_sort,
            "merge": self.merge_sort,
            "quick": self.quick_sort,
            "heap": self.heap_sort,
        }
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        pygame.display.set_icon(self.ICON)
        self.running = True
        self.main()

    def draw_buttons(self):
        """Drawing the buttons for the pygame GUI
        """
        pygame.draw.rect(self.display, WHITE, self.slide_bar)
        for tick, size in zip(self.tick_list, self.tick_size):
            if self.length == size:
                color = BLACK
            else:
                color = LIGHT_GREY
            pygame.draw.rect(self.display, color, tick)

        font = pygame.font.SysFont("calibri", 20)
        for but, content in zip(self.but_list, self.but_order):
            if but.collidepoint(pygame.mouse.get_pos()):
                color = LIGHT_GREY
            else:
                color = WHITE
            pygame.draw.rect(self.display, color, but)
            text = font.render(content, True, BLACK)
            text_x = but.centerx - text.get_width() // 2
            text_y = but.centery - text.get_height() // 2
            self.display.blit(text, (text_x, text_y))

        text = font.render("small", True, BLACK)
        text_x = int(self.SLIDE_X - text.get_width() * 1.5)
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("big", True, BLACK)
        text_x = int(self.SLIDE_X + self.SLIDE_SPACING * 5 + 10 + text.get_width())
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

    def update_gui(self, one=None, two=None, three=None, done=False, sorting=False):
        """Refresh the pygame GUI window

        Args:
            one (int, optional): index to be colored yellow. Defaults to None.
            two (int, optional): index to be colored yellow. Defaults to None.
            three (int, optional): index to be colored green. Defaults to None.
            done (bool, optional): True if sorting has finished, else False. Defaults to False.
            sorting (bool, optional): True if list is being sorted, else False. Defaults to False.
        """
        self.display.fill(GREY)

        self.draw_buttons()

        wid = 1024 / self.length
        space = self.WIDTH / self.length
        hei = 128 / self.length

        for i, elem in enumerate(self.array):
            if i in (one, two):
                color = YELLOW
            elif i == three:
                color = GREEN
            else:
                color = BLUE

            if done:
                color = GREEN
            pygame.draw.rect(self.display, color, (i * space, 0, wid, elem * hei))

        if sorting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.display.update()

    def mouse_click(self, pos):
        """Detecting which button the user pressed

        Args:
            pos (tuple): pos[0] is the x coordinate, pos[1] is the y coordinate
        """
        if self.regen_but.collidepoint(pos):
            self.reinitialize_arr(self.length)
        for but, content in zip(self.but_list[1:], self.but_order[1:]):
            if but.collidepoint(pos):
                self.sorted = False
                self.sort_dict[content]()

        for tick, size in zip(self.tick_list, self.tick_size):
            if tick.collidepoint(pos):
                self.reinitialize_arr(size)

    def main(self):
        """Main function of this module
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click(pygame.mouse.get_pos())

            if self.sorted:
                self.update_gui(done=True)
            else:
                self.update_gui()
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    vis = AlgoVisualizer()
