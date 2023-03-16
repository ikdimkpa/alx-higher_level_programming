#!/usr/bin/python
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list

    new_lst = [elem if elem != search else replace for elem in my_list]
    return new_lst