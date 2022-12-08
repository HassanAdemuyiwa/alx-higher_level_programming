#!/usr/bin/python3
''' Code to print list of integers '''


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
