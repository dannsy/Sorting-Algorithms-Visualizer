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
    slide_bar = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_SPACING * 5 + 10, BUT_HEIGHT)
    size_32 = pygame.Rect(SLIDE_X, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_64 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 1, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_128 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 2, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_256 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 3, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_512 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 4, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)
    size_1024 = pygame.Rect(SLIDE_X + SLIDE_SPACING * 5, BUT_Y, SLIDE_WIDTH, BUT_HEIGHT)

    ICON = pygame.image.load(os.path.join(os.getcwd(), "assets", "img", "chart.jpg"))

    def __init__(self):
        super().__init__(128, True)
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        pygame.display.set_icon(self.ICON)
        self.running = True
        self.main()

    def draw_buttons(self):
        """Drawing the buttons for the pygame GUI
        """
        if self.regen_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.regen_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.regen_but)
        if self.select_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.select_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.select_but)
        if self.insert_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.insert_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.insert_but)
        if self.merge_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.merge_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.merge_but)
        if self.quick_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.quick_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.quick_but)
        if self.heap_but.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, LIGHT_GREY, self.heap_but)
        else:
            pygame.draw.rect(self.display, WHITE, self.heap_but)

        pygame.draw.rect(self.display, WHITE, self.slide_bar)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_32)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_64)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_128)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_256)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_512)
        pygame.draw.rect(self.display, LIGHT_GREY, self.size_1024)
        if self.length == 32:
            pygame.draw.rect(self.display, BLACK, self.size_32)
        elif self.length == 64:
            pygame.draw.rect(self.display, BLACK, self.size_64)
        elif self.length == 128:
            pygame.draw.rect(self.display, BLACK, self.size_128)
        elif self.length == 256:
            pygame.draw.rect(self.display, BLACK, self.size_256)
        elif self.length == 512:
            pygame.draw.rect(self.display, BLACK, self.size_512)
        elif self.length == 1024:
            pygame.draw.rect(self.display, BLACK, self.size_1024)

        font = pygame.font.SysFont("calibri", 20)
        text = font.render("regenerate", True, BLACK)
        text_x = self.REGEN_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("selection", True, BLACK)
        text_x = self.SELECT_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("insertion", True, BLACK)
        text_x = self.INSERT_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("merge", True, BLACK)
        text_x = self.MERGE_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("quick", True, BLACK)
        text_x = self.QUICK_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
        self.display.blit(text, (text_x, text_y))

        text = font.render("heap", True, BLACK)
        text_x = self.HEAP_BUT_X + (self.BUT_WIDTH - text.get_width()) // 2
        text_y = self.BUT_Y + (self.BUT_HEIGHT - text.get_height()) // 2
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
        elif self.select_but.collidepoint(pos):
            self.sorted = False
            self.selection_sort()
        elif self.insert_but.collidepoint(pos):
            self.sorted = False
            self.insertion_sort()
        elif self.merge_but.collidepoint(pos):
            self.sorted = False
            self.merge_sort()
        elif self.quick_but.collidepoint(pos):
            self.sorted = False
            self.quick_sort()
        elif self.heap_but.collidepoint(pos):
            self.sorted = False
            self.heap_sort()
        elif self.size_32.collidepoint(pos):
            self.reinitialize_arr(32)
        elif self.size_64.collidepoint(pos):
            self.reinitialize_arr(64)
        elif self.size_128.collidepoint(pos):
            self.reinitialize_arr(128)
        elif self.size_256.collidepoint(pos):
            self.reinitialize_arr(256)
        elif self.size_512.collidepoint(pos):
            self.reinitialize_arr(512)
        elif self.size_1024.collidepoint(pos):
            self.reinitialize_arr(1024)

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
