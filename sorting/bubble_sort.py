def bubble_sort(my_list: list) -> list:
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                greater = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = greater
    return my_list
