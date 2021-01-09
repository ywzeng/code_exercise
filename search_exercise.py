# -*- coding: utf-8 -*-

"""
@author: zyw
@file: search_exercise.py
@time: 2021/1/9
"""


def binary_search(data_list, data):
    """ The data list should be ordered (ascending order in default). """
    if not data_list:
        return
    if data > data_list[-1] or data < data_list[0]:
        return
    mid_index = len(data_list) // 2
    if data_list[mid_index] == data:
        return data
    else:
        if data < data_list[mid_index]:
            return binary_search(data_list[:mid_index], data)
        else:
            return binary_search(data_list[mid_index+1:], data)


class HashTable(object):
    def __init__(self, size):
        """ Initialize the size and the default value of hash table. """
        self.data_list = [None for i in range(size)]
        self.size = size        # The max length of the hash table.

    def hash(self, data) -> int:
        """ Calculate the hash value of the give data. """
        return data % self.size     # The data has the same mod value will has the same hash value.

    def insert_hash(self, data) -> bool:
        """ Insert the data into the hash table. The index of this data in the hash table is its hash value. """
        hash_value = self.hash(data)
        original_hash = hash_value
        # Hash conflict. Namely if the hash address has already been used, move to next address.
        while self.data_list[hash_value]:
            hash_value = (hash_value + 1) % self.size
            if self.data_list[hash_value] or hash_value == original_hash:
                print('No available space. Insert Failed!')
                return False
        self.data_list[hash_value] = data
        print('Insert successfully!')
        return True

    def search_hash(self, data) -> bool:
        """ Search the data in the hash table. """
        hash_value = self.hash(data)
        original_hash = hash_value
        while self.data_list[hash_value] != data:
            hash_value = (hash_value + 1) % self.size
            if not self.data_list[hash_value] or hash_value == original_hash:
                print('No such data in the hash table.')
                return False
        print('The data is in the hash table.')
        return True


if __name__ == '__main__':
    data_list = [4, 8, 1, 2]
    hash_table = HashTable(4)
    for data in data_list:
        hash_table.insert_hash(data)
    print(hash_table.data_list)