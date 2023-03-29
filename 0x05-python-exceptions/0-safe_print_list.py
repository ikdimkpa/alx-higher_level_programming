#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = 0
    for i in range x:
        try:
            print(f"{my_list[elem]}", end="")
            new_list += 1
        except IndexError:
            break
    print()
    return new_list
