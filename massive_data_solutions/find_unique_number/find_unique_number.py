# -*- coding: utf-8 -*-

from bitarray import bitarray
from ..utils.utils import gen_numbers

# 00 不存在
# 01 出现一次
# 10 出现多次
# 11 无意义

MIN = 0
MAX = 100000000
NUM_COUNT = 100000

bit_array = bitarray(MAX * 2)
bit_array.setall(0)


def run():
    num_unique = 0
    for num in gen_numbers(MIN, MAX, NUM_COUNT):
        set_bit(num)
    bit_str = bit_array.to01()
    for i in range(MAX):
        start = i * 2
        end = i * 2 + 1
        if bit_str[start:end+1] == '01':
            num_unique += 1
    print('存在{}个唯一的数'.format(num_unique))


def set_bit(num):
    start = num * 2
    end = num * 2 + 1

    if bit_array[start] == 0 and bit_array[end] == 0:
        # 不存在->出现一次(00->01)
        bit_array[end] = 1
    elif bit_array[start] == 0 and bit_array[end] == 1:
        # 出现一次->出现多次(01->10)
        bit_array[start] = 1
        bit_array[end] = 0
    elif bit_array[start] == 1 and bit_array[end] == 0:
        # 出现多次->出现多次(10->10)
        pass
