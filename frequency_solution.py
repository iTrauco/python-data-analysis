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
num_user_ratings = [] 

for row in apps_data[1:]:
    num_user_ratings.append(int(row[5]))
    
# print(num_user_ratings[2])
# print(len(num_user_ratings))
max_value = max(num_user_ratings)
min_value = min(num_user_ratings)
# print(max_value)
# print(min_value)
# choose at three interval ranges
user_ratings_frequency = {'0 - 500000': 0, '500000 - 1500000': 0, '1500000 - 3000000': 0}
# print(user_ratings_frequency)
#print(type(user_ratings_frequency))
# compute the frequency of apps for each interval 
for row in apps_data[1:]:
    user_ratings = int(row[5])

    if user_ratings <= 1000:
        user_ratings_frequency['0 - 500000'] += 1
        
    elif 500000 < user_ratings <= 1500000:
        user_ratings_frequency['500000 - 1500000'] += 1

    elif 1500000 < user_ratings <= 3000000:
        user_ratings_frequency['1500000 - 3000000'] += 1

print(user_ratings_frequency)
