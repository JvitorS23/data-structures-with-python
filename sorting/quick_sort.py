def swap(my_list, index_1, index_2):
    temp = my_list[index_1]
    my_list[index_1] = my_list[index_2]
    my_list[index_2] = temp


def pivot(my_list, pivot_index, end_index) -> int:
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list: list, start: int, end: int) -> list:
    if start < end:
        pivot_index = pivot(my_list, start, end)
        quick_sort_helper(my_list, start, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, end)
    return my_list


def quick_sort(my_list: list) -> list:
    return quick_sort_helper(my_list, 0, len(my_list) - 1)
