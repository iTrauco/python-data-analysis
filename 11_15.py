#!/usr/bin/env python3
# -*- coding: utf-8 -*-

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions = {}

for key in content_ratings:
    proportion = content_ratings[key] / total_number_of_apps
    print('Key:', key)
    print('Proportion Value:', proportion)

    c_ratings_proportions[key] = proportion
    print(c_ratings_proportions)

