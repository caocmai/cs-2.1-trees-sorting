#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n + k) where k is the range of numbers, because if k is really high then affects the run time significantly. 
    Memory usage: O(k) because the number of total arrays is equal to the value of k"""

    # the baisc concept of counting sort is creating a very large array and then assoiating each value in the list to be sorted to the temp's array index. For example, if you wanted to sort 3, 1, 2 to 1,2,3 then 3 is 3rd index, 2=2nd index, 1=1st index
    # drawback - negative numbers doesn't currently work.

    # creating a temp array with 0, times howevery many based on the max value of numbers + 1
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

# bucket index formula from https://www.cs.usfca.edu/~galles/visualization/BucketSort.html
def bucket_index_formula(num, numbers):
    maximum_number = max(numbers)
    bucket_index = num * len(numbers) / (maximum_number + 1)

    return int(bucket_index)

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k) where k is the number of buckets. The time complexity is depended on both
    n and k because if k is large then our algorithm is also increased because we have to traverse the buckets
    Memory usage: O(n) because as the n increases the space increases linearly, we are not doing processes in place so space is increased with n"""

    # creating the buckets, in this case it's a list within a list
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    # loop through all the numbers
    for num in numbers:
        # determine the bucket index; using a given formula
        b_index = bucket_index_formula(num, numbers)
        # add to bucket
        buckets[b_index].append(num)
        # note: ultimately we want to sort this list but we will do that later

    # initialize empty bucket list
    complete_sorted_list = []
    # loop through bucket list with lists
    for array in buckets:
        # extend the list of the bucket into the complete sorted list if it's not empty
        if array != []:
            # sort then extend to completed_sorted_list 
            insertion_sort(array)
            complete_sorted_list.extend(array)
    return complete_sorted_list