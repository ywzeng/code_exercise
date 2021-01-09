# -*- coding: utf-8 -*-

"""
@author: zyw
@file: sort_algorithm.py
@time: 2021/1/7
"""


def bubble_sort(data_list):
    for i in range(len(data_list)-1):
        for j in range(len(data_list)-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    print(data_list)
    return data_list


def select_sort(data_list):
    """
    Find the smallest data in [0:], and put it on the first index ([0]) of [0:]. Namely, swap it with the data at [0].
    Then, find the smallest data in [1:], and put it on the first index of [1:].
    ...
    We need a variable to indicate the index of the swapped data.
    """
    for i in range(len(data_list)-1):
        min_index = i+1       # Indicate the index of the minimum data in the sub-list [i:].
        for j in range(i+1, len(data_list)):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if data_list[min_index] < data_list[i]:
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    print(data_list)
    return data_list


def insert_sort(data_list):
    """
    Form a ordered sequence, and injected data into this sequence from a unordered sequence.
    Divide the original data list into two dynamic sub-list, the front is the ordered sequence and the remaining is the unordered sequence.
    """
    for i in range(1, len(data_list)):
        # Compare [j] with [j-1], and swap the two data if [j] is smaller than the [j-1].
        # Here, [j] is in [0: i]
        # This swap part is somewhat similar with the bubble-sort algorithm.
        print(data_list[:i+1], data_list[i+1:])
        for j in range(i, 0, -1):
            if data_list[j] < data_list[j-1]:
                data_list[j-1], data_list[j] = data_list[j], data_list[j-1]
        print(data_list[0:i+1], data_list[i+1:], '\n')
    print(data_list)
    return data_list


def quick_sort_recursion(data_list):
    """
    Given a list, use a data within it as the partition data.
    Then, move the data in this list, making the the data in the left of partition are all smaller than the partition, and the data in the right of partition are all bigger than the partition.
    Divide the list into three part: left sub-list, mid value, and right sub-list
    :return:
    """
    if len(data_list) < 2:
        return data_list
    mid_index = len(data_list) // 2
    mid_data = data_list.pop(mid_index)
    left_sub_list, right_sub_list = [], []
    for data in data_list:
        if data <= mid_data:
            left_sub_list += [data]
        else:
            right_sub_list += [data]
    left_sub_list = quick_sort_recursion(left_sub_list)
    right_sub_list = quick_sort_recursion(right_sub_list)
    return left_sub_list + [mid_data] + right_sub_list


def hill_sort(data_list):
    """
    Hill sort is a special case of insert sort. But they are different in step width.
    Hill sort has a dynamic step width which mostly start with length/2 and decrease by 1/2 in each time. It is called Hill Increment.
    The step here means that the two numbers that are N steps apart will be divided into one set.
    For example, [6,5,4,3,2,1], step is 3. So the partition results are: [6, 3], [5, 2], [4, 1].
    Then, we directly use the insert_sort algorithm on these partitions, getting [3, 6], [2, 5], and [1, 4]. Get [3,2,1,6,5,4].
    Then, we decrease the step width to 3/2, namely 1. So the partition result is [3,2,1,6,5,4].
    Then, we directly use the insert_sort algorithm on this partition, getting [1, 2, 3, 4, 5, 6].
    :param data_list:
    :return:
    """
    step = len(data_list) // 2      # incremental factor, decreasing 1/2 each time.
    while step:
        for cursor in range(step, len(data_list)):
            i = cursor
            # Insert sort of the sub-partition. Only sort the [:cursor] part of the partition.
            # partition = [..., i-step, i, i+step, ...]
            # The visible part of the partition is keeping wider with the backward move of the 'cursor' index.
            while i >= step and data_list[i] < data_list[i-step]:
                # swap the two data if the front one is bigger than the behind one.
                data_list[i-step], data_list[i] = data_list[i], data_list[i-step]
                i -= step
        step = step // 2
    print(data_list)
    return data_list


if __name__ == '__main__':
    data_list = [3, 6, 4, 2, 11, 10, 5]
    hill_sort(data_list)