#!/usr/bin/python3
def safe_print_list(my_list, x):
    new_list = 0
    for elem in my_list:
        if new_list == x:
            break
        new_list += 1
        print(elem,end="")
        try:
            print(f"{my_list[elem]}", end="")
        except IndexError:
            break
    print("")
    return new_list
