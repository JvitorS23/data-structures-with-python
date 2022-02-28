def selection_sort(my_list: list) -> list:
    for i in range(len(my_list) - 1):
        min_value = my_list[i]
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < min_value:
                min_value = my_list[j]
                min_index = j
        if i != min_index:
            my_list[min_index] = my_list[i]
            my_list[i] = min_value
    return my_list
