#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []

    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list.append(res)
        except ZeroDivisionError:
            print('division by 0')
            new_list.append(0)
        except TypeError:
            print('wrong type')
            new_list.append(0)
        except IndexError:
            print('out of range')
            new_list.append(0)
        finally:
            i += 1

    return new_list
