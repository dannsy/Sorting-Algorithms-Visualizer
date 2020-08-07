"""This module contains the Algorithms class which houses my implementation
for some popular sorting algorithms.
"""
import random
import time

ARR_SIZE = 8192


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

    def __init__(self, arr_size, visualize=False):
        self.arr_size = arr_size
        self.array = random.sample(range(arr_size * 4), arr_size)
        self.length = len(self.array)
        self.visualize = visualize
        self.sorted = False

    def update(self, one=None, two=None, three=None):
        """Send sorting state to visualize
        """
        import visualizer

        visualizer.update_gui(self.array, self.arr_size, one, two, three, sorting=True)

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


if __name__ == "__main__":
    algo = Algorithms(ARR_SIZE)
    copy_array = algo.array.copy()
    # print(copy_array)
    algo.heap_sort()
    # print(algo.array)

    print(check_sort_validity(copy_array, algo.array))
