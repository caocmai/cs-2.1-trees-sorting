#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because at most loop through the entire array
    Memory usage: O(1) because not creating any new space and everything is done in place"""
    for i in range(len(items) - 1):
        if items[i+1] < items[i]:
            return False
    return True

    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: o(n^2) because as the input grows so does both of the loops
    Memory usage: O(1) because not creating any new space and everything is done in place"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    array_length = len(items) - 1
    
    while array_length > 0:
        swap = False
        for i in range(array_length):
            if items[i+1] < items[i]:
                items[i], items[i+1] = items[i+1], items[i]
                swap = True
        if not swap:
            break
        array_length -= 1

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) because as the numbers of items grow the so does the outter and inner loop
    Memory usage: O(1) because as items grow no additional spaces are created and everything done in place"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    start_index = 0
    while start_index < len(items) - 1:
        lowest_index = start_index
        for i in range(start_index, len(items) - 1):
            if items[i] < items[start_index]:
                lowest_index = i
        start_index += 1

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
