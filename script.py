#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import reader function from csv module
from csv import reader
# open file
opened_file = open('AppleStore.csv')
# read the contents of the file
read_file = reader(opened_file)
# transform file contents into a list of lists
apps_data = list(read_file)

# find minimum and maximum in rating_count_column
n_user_ratings = []
for row in rating_count_tot:
    n_user_ratings[5] = float

