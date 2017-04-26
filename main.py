# -*- coding: utf-8 -*-

import timeit
from massive_data_solutions.find_unique_number.find_unique_number import run

t = timeit.Timer(stmt=run)
print('[consume time: {}]'.format(t.timeit(1)))

