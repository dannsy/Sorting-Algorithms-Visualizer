"""This module contains the Algorithms class which houses my implementation
for some popular sorting algorithms.
"""
import os
import random
import time
from collections import namedtuple

import pygame

Color = namedtuple("Color", ["r", "g", "b"])
WHITE = Color(255, 255, 255)
GREY = Color(160, 160, 160)
LIGHT_GREY = Color(210, 210, 210)
BLUE = Color(80, 230, 230)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 0, 0)


def _timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, *kwargs)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"Time elapsed for {func.__name__}: {time_elapsed}")

    return wrapper


def check_sort_validity(orig_arr, sorted_arr):
    """Helper function to check whether an implemented sorting algorithm
    is valid

    Args:
        orig_arr (list): The original list
        sorted_arr (list): The sorted list

    Returns:
        bool: Whether using the python built-in sorted function yields the
        same list as the sorted list
    """
    return sorted(orig_arr) == sorted_arr


class Algorithms:
    """This class contains my implementation of some common sorting
    algorithms, as well as a visualizer made with pygame
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

    def __init__(self, arr_size, visualize=False):
        if visualize:
            arr_size = 128
        self.array = random.sample(range(arr_size * 4), arr_size)
        self.length = arr_size
        self.visualize = visualize
        self.sorted = False

        if visualize:
            pygame.init()
            self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            pygame.display.set_caption("Sorting Algorithm Visualizer")
            pygame.display.set_icon(self.ICON)
            self.running = True
            self.main()

    def reinitialize_arr(self, arr_size):
        """Reinitialize the list to specified size

        Args:
            arr_size (int): new size of list
        """
        self.sorted = False
        self.array = random.sample(range(arr_size * 4), arr_size)
        self.length = arr_size

    def update(self, one=None, two=None, three=None):
        """Send sorting state to visualize
        """
        self.update_gui(one, two, three, sorting=True)

    @_timer
    def selection_sort(self):
        """Implementation of the selection sort algorithm
        """
        for i in range(self.length):
            min_index = i
            for j in range(i + 1, self.length):
                # finding minimum element
                if self.array[j] < self.array[min_index]:
                    min_index = j
                if self.visualize:
                    self.update(i, j, min_index)
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

        self.sorted = True

    @_timer
    def insertion_sort(self):
        """Implementation of the insertion sort algorithm
        """
        for i in range(self.length):
            cur_elem = self.array[i]
            while i >= 1:
                if cur_elem < self.array[i - 1]:
                    # sliding element to rightful index
                    self.array[i] = self.array[i - 1]
                    i -= 1

                    if self.visualize:
                        self.update(i)
                else:
                    break
            self.array[i] = cur_elem

        self.sorted = True

    @_timer
    def merge_sort(self):
        """Middle function to call the actual merge sort function
        """
        self.help_merge_sort(0, self.length)

        self.sorted = True

    def help_merge_sort(self, start, end):
        """Implementation of the merge sort algorithm

        Args:
            start (int): start index of the list
            end (int): end index of the list
        """
        middle = (start + end) // 2

        # divide and conquer
        if middle - start > 1:
            self.help_merge_sort(start, middle)
        if end - middle > 1:
            self.help_merge_sort(middle, end)

        if self.visualize:
            self.merge(start, middle, end)
        else:
            self.faster_merge(start, middle, end)

    def merge(self, start, middle, end):
        """Helper function for merge sort to merge two lists.
        Visualize version

        Args:
            start (int): start index of the list
            middle (int): middle index of the list
            end (int): end index of the list
        """
        first_arr = self.array[start:middle].copy()
        second_arr = self.array[middle:end].copy()
        i, j = 0, 0
        while i < len(first_arr) and j < len(second_arr):
            # merging split arrays in a sorted manner
            if first_arr[i] < second_arr[j]:
                self.array[start + i + j] = first_arr[i]
                i += 1
                self.update(start + i + j)
            else:
                self.array[start + i + j] = second_arr[j]
                j += 1
                self.update(start + i + j)

        # whichever array has leftover will be appended to the merged array
        while i < len(first_arr):
            self.array[start + i + j] = first_arr[i]
            i += 1
            self.update(start + i + j)
        while j < len(second_arr):
            self.array[start + i + j] = second_arr[j]
            j += 1
            self.update(start + i + j)

    def faster_merge(self, start, middle, end):
        """Helper function for merge sort to merge two lists

        Args:
            start (int): start index of the list
            middle (int): middle index of the list
            end (int): end index of the list
        """
        new_arr = []
        first_arr = self.array[start:middle]
        second_arr = self.array[middle:end]
        i, j = 0, 0
        while i < len(first_arr) and j < len(second_arr):
            # merging split arrays in a sorted manner
            if first_arr[i] < second_arr[j]:
                new_arr.append(first_arr[i])
                i += 1
            else:
                new_arr.append(second_arr[j])
                j += 1

        # whichever array has leftover will be appended to the merged array
        while i < len(first_arr):
            new_arr.append(first_arr[i])
            i += 1
        while j < len(second_arr):
            new_arr.append(second_arr[j])
            j += 1

        self.array[start:end] = new_arr

    @_timer
    def quick_sort(self):
        """Middle function to call the actual quick sort function
        """
        self.help_quick_sort(0, self.length - 1)

        self.sorted = True

    def help_quick_sort(self, start, end):
        """Implementation of the quick sort algorithm

        Args:
            start (int): start index of the list
            end (int): end index of the list (inclusive)
        """
        if start < end:
            pivot = self.partition(start, end)

            # divide and conquer
            self.help_quick_sort(start, pivot - 1)
            self.help_quick_sort(pivot + 1, end)

    def partition(self, start, end):
        """Helper function for quick sort to partition and pivot the list

        Args:
            start (int): start index of the list
            end (int): end index of the list

        Returns:
            int: final index of the pivot
        """
        # pivot will be the last element in list
        pivot = self.array[end]
        i = start

        for j in range(start, end):
            if self.array[j] < pivot:
                if i != j:
                    # placing elements smaller than pivot on left side
                    self.array[i], self.array[j] = self.array[j], self.array[i]

                    if self.visualize:
                        self.update(i, end)
                i += 1

        # pivot placed on correct index
        self.array[i], self.array[end] = self.array[end], self.array[i]
        return i

    @_timer
    def heap_sort(self):
        """Implementation of the heap sort algorithm
        """
        # building a maxheap
        for index in range(self.length // 2 - 1, -1, -1):
            self.heapify_down(index, self.length)

        # repeatedly remove max and rebuild heap
        for index in range(self.length - 1, -1, -1):
            self.array[0], self.array[index] = self.array[index], self.array[0]
            self.heapify_down(0, index)

        self.sorted = True

    def heapify_down(self, index, length):
        """Swaps a parent with left or right child if the biggest child
        is bigger than the parent

        Args:
            index (int): index of the parent
        """
        if self.visualize:
            self.update(index)

        current = self.array[index]
        left_index = 2 * index + 1
        if left_index >= length:
            # left child doesn't exist, heapify done
            return

        right_index = 2 * index + 2
        left_child = self.array[left_index]
        if right_index >= length:
            # right child doesn't exist, only need to compare left child
            if current > left_child:
                # left child smaller
                return
            self.array[index], self.array[left_index] = left_child, current
            return

        right_child = self.array[right_index]
        if current > left_child and current > right_child:
            # parent bigger than both children, heapify done
            return

        max_child = None
        max_index = None
        # finding the bigger child
        if self.array[left_index] < self.array[right_index]:
            max_child = self.array[right_index]
            max_index = right_index
        else:
            max_child = self.array[left_index]
            max_index = left_index

        if current < max_child:
            # parent is smaller than bigger child, swap places
            self.array[index], self.array[max_index] = max_child, current

        # continue heapify down on swapped parent
        self.heapify_down(max_index, length)

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
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click(pygame.mouse.get_pos())

            if self.sorted:
                self.update_gui(done=True)
            else:
                self.update_gui()
            pygame.display.update()


if __name__ == "__main__":
    array_size = 8192
    algo = Algorithms(array_size, True)
    copy_array = algo.array.copy()
    # print(copy_array)
    # algo.heap_sort()
    # print(algo.array)

    # print(check_sort_validity(copy_array, algo.array))
