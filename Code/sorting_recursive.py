#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    merge_list = []
    index_items1 = 0
    index_items2 = 0
    
    # comparing both lists and adding the element to the merge_list or know the point where both list are in order, this loop stops when you have completely travase one of the arrays to merge
    while index_items1 < len(items1) and index_items2 < len(items2):
        # compare the two sorted arrays, items1 and items2
        if items1[index_items1] < items2[index_items2]:
            # element in items1 is smaller than items 2 so append to merge_list
            merge_list.append(items1[index_items1])
            index_items1 += 1
        else:
            # element in items1 is greater than items 2 so append element of items2 to list
            merge_list.append(items2[index_items2])
            index_items2 += 1

    # add whatever is left because in our while loop we stop the moment either the index left or index right is > len(items)
    merge_list += items1[index_items1:]
    merge_list += items2[index_items2:]

    return merge_list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlogn) becuase breaking the list down every time; divide and conquer
    Memory usage: O(n) because calling function resursively so just grows linearyly with input"""

    if items == []:
        return items

    # base case in recursive call
    if len(items) == 1:
        return items

    mid = len(items) // 2
    left = items[0:mid]
    right = items[mid:]

    # return merge(merge_sort(left), merge_sort(right))
    # this so it's manipulating the items array instead of returning a new array
    items[:] = merge(merge_sort(left), merge_sort(right))
    return items[:]

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pass


def quick_sort(arr, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(nlogn) because your unsort list gets smaller and smaller with each recursive call
    Worst case running time: O(n^2) when you pick all high numbers then you need to traverse entire length of array and made only progress sorting on that highest number.
    Memory usage: O(n) because calling function recursively"""

    # base case in recursive call <=1 because last element is the pivot and poping it 
    if len(arr) <= 1:
        return arr
    else:
        # pops first item until len(arr) is 1 or less
        pivot = arr.pop(0)
    
        items_greater = []
        items_lower = []

        for num in arr:
            if num > pivot:
                items_greater.append(num)
            else:
                items_lower.append(num)
    
        # just so to get to pass sorting_test.py by mutating original array
        arr[:] = quick_sort(items_lower) + [pivot] + quick_sort(items_greater)    
        return arr[:]

