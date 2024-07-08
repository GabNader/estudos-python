# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.
from itertools import count
str_x = 'Emma is good developer. Emma is a writer'
times = str_x.count('Emma')
print(f'Emma appeared {times} times')
