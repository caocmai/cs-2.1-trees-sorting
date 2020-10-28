#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because at most loop through the entire array
    Memory usage: O(1) because not creating any new space and everything is done in place"""
    for i in range(len(items) - 1):
        # if next item is smaller than current, then list not sorted
        if items[i+1] < items[i]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: o(n^2) because as the input grows so does both of the loops
    Memory usage: O(1) because not creating any new space and everything is done in place"""
    array_length = len(items) - 1
    
    # goes through the list and looks at the next item and if it's smaller than current item then swap, else it continues down the list. The loop is repeated however many times it needs to and stops when no swapping occurs. 
    # the number of passes that needs to go before instance of no swap or go through each item with one pass
    while array_length > 0:
        swap = False
        for i in range(array_length):
            if items[i+1] < items[i]:
                items[i], items[i+1] = items[i+1], items[i]
                swap = True
        # the while loop breaks if during this pass there was not a swap
        if not swap:
            break
        array_length -= 1

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) because as the numbers of items grow the so does the outter and inner loop
    Memory usage: O(1) because as items grow no additional spaces are created and everything done in place"""

    # pseudo seperates list into 2 sections, sorted and unsorted, goes through the unsorted section and finds the index with lowest value among all and swaps it with the sorted section

    ## can use while or for outter loop
    # i = 0
    # this is 'sorted' section
    # while i < len(items) - 1:
    for i in range(len(items)-1):
        lowest_index = i
        lowest_value = items[lowest_index]
        # this is 'unsorted' section
        for j in range(lowest_index + 1, len(items)):
            if items[j] < lowest_value:
                # lowest_index gets updated and settles with the lowest index of lowest value
                lowest_index = j
                lowest_value = items[j]
        # performs the swap
        items[i], items[lowest_index] = items[lowest_index], items[i]
        # moves pointer up
        # i += 1

    return items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n) because as items grow outter and inner loop both increases
    Memory usage: O(1) because everything is done in place """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

    # similar to selection sort where list is pseudo broken into 'sorted' and 'unsorted' sections
    # an item is selected from 'unsorted' and checks against the 'sorted' section to see where to add

    # this is our selection section of the list
    for i in range(1, len(items)):
        # range is non inclusive so i is never reached only i-1
        # loop through our 'sorted' section
        for j in range(0, i):
            # the moment it finds an item in this part of the list which is greater or equal 'unsorted' selected item, it is removed from the 'unsorted' section and inserted into the 'sorted' section
            if items[j] >= items[i]:
                removed_item = items.pop(i)
                items.insert(j, removed_item)
                # can continue/skip loop cause this part of the list is sorted, which means everything after will be much larger than selected item
                continue
    return items
