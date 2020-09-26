#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import reader from csv module
from csv import reader
# open csv 
open_file = open('AppleStore.csv')
# read file
read_file = reader(open_file)
# read data as a list of lists
apps_data = list(read_file)
# create empty dictionary
genre_counting = {}

# loop through apps_data
for row in apps_data[1:]:
    # assigns index value 11 to genre variable
    genre = row[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1

print(genre_counting)

    
