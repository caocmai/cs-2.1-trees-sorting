#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    result = []
    index_left = 0
    index_right = 0
    
    while index_left < len(items1) and index_right < len(items2):
        if items1[index_left] < items2[index_right]:
            result.append(items1[index_left])
            index_left += 1
        else:
            result.append(items2[index_right])
            index_right += 1

    result.extend(items1[index_left:])
    result.extend(items2[index_right:])

    return result

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if items == []:
        return items

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
    pivot = items[low]
    start = low
    end = high - 1

    while start <= end:
        while start <= high and items[start] < pivot:
            start += 1
        while end >= start and items[end] >= pivot:
            end -= 1
        if start < end:
            items[end], items[start] = items[start], items[end]
        else:
            items[high], items[start] = items[start], items[high]

    return end


def quick_sort(arr, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    
    # low = 0
    # high = len(items) - 1

    # if low >= high:
    #     return

    # if low < high:
    #     loc = partition(items, low, high)
    #     quick_sort(items, low, loc - 1)
    #     quick_sort(items, loc + 1, high)

