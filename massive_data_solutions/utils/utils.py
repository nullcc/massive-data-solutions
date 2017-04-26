# -*- coding: utf-8 -*-

import random


def gen_numbers(min, max, count):
    """
    整型数生成器,生成count个范围在[min, max)中的整数
    :param min:
    :param max:
    :param count:
    :return:
    """
    for i in range(count):
        yield random.randint(min, max - 1)
