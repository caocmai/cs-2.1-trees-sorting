#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # creating a temp array with [0] times howevery many based on the max value of numbers
    temp_array = [0] * (max(numbers) + 1)
    # loop through numbers
    for num in numbers:
        # if the temp array's index of that number is 0 - meaning it's empty then set it to be 1
        if temp_array[num] == 0:
            temp_array[num] = 1
        # else there's already something in there so just add one to it
        else:
            temp_array[num] += 1

    numbers = []

    # loop through the temp_array
    for y in range(len(temp_array)):
        # if it's index is not equal to 0 then we add the count; and looping until it's index value is 0
        while temp_array[y] != 0:
            numbers.append(y)
            temp_array[y] -= 1

    return numbers

def bucket_index_formula(num, numbers):
    maximum_number = max(numbers)
    bucket_index = num * len(numbers) / (maximum_number + 1)

    return int(bucket_index)

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    # creating the buckets, in this case it's a list within a list
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    # loop through all the numbers
    for num in numbers:
        # determin the bucket index
        b_index = bucket_index_formula(num, numbers)
        # add to bucket
        buckets[b_index].append(num)
        # sort bucket
        insertion_sort(buckets[b_index])

    # initialize empty bucket list
    complete_sorted_list = []
    # loop through bucket list with lists
    for array in buckets:
        # extend the list of the bucket into the complete sorted list if it's not empty
        if array != []:
            complete_sorted_list.extend(array)
    return complete_sorted_list
        
test = [2,22,5,3,4,400, 34, 234, 54, 34]


print(bucket_sort(test))