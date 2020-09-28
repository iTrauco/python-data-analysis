#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file) 

data_sizes = []

for row in apps_data[1:]:
    size = float(row[2])
    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)

print(min_size)
print(max_size)
