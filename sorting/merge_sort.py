def merge(list1: list, list2: list) -> list:
    sorted_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1
    return sorted_list


def merge_sort(my_list: list) -> list:
    if len(my_list) == 1 or len(my_list) == 0:
        return my_list
    half = int(len(my_list) / 2)
    left = my_list[:half]
    right = my_list[half:]
    return merge(merge_sort(left), merge_sort(right))
