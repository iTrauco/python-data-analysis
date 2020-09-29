#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

#print(data_sizes['0 - 10 MB'])
#!print(type(data_sizes))
#print(type(data_sizes['10 - 50 MB']))
#print(float(data_sizes['10 - 50 MB']))

# size_freq = {}

#print(size_freq)
#print(type(size_freq))


# for row in apps_data[1:]:
  #  size = row[2]
data_sizes = {'0 - 10 MB': 0, '10 - 50 MB': 0, '50 - 100 MB': 0, '100 - 500 MB': 0, '500 MB+': 0}

for row in apps_data[1:]:
    data_size = float(row[2])
    if data_size <= 10000000:
        data_sizes['0 - 10 MB'] += 1

    elif 10000000 < data_size <= 50000000:
        data_sizes['10 - 50 MB'] += 1

    elif 50000000 < data_size <= 100000000:
        data_sizes['50 - 100 MB'] += 1

    elif 100000000 < data_size <= 500000000:
        data_sizes['100 - 500 MB'] += 1

    elif data_size > 500000000:
        data_sizes['500 MB+'] += 1

data_sizes
