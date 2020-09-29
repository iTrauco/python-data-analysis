#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
#########################################
# import csv's reader
from csv import reader
# open file
opened_file = open('AppleStore.csv')
# read file contents
read_file = reader(opened_file)
# transform contents into list of lists
apps_data = list(read_file)
#print(type(apps_date))
#print(len(apps_date))
#########################################
#########################################
# 1.find min and max values of rating_count_tot
ratings = {}

for row in apps_data[1:]:
    ratings = int(row[5])
    
# print(number_of_ratings)
# print(type(num_of_ratings))
max_value = max(num_of_ratings)
print(max(num_of_ratings))
# choose at least five intervals

# compute the frequency of apps for each interval 

# store frequency table in a dictionary
# interval are the keys with a value of zero

# count the frequency of each interval in apps_date(if/elif)

# review results



