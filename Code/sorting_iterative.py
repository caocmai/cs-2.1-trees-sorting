#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because at most loop through the entire array
    Memory usage: O(1) because not creating any new space"""
    for i in range(len(items) - 1):
        if items[i+1] < items[i]:
            return False
    return True

    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: o(n^2) because as the input grows so does both of the loops
    Memory usage: O(1) because not creating any new space"""
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
