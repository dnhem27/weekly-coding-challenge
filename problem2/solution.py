def find_missing_element(old_array, new_array):
    missing_element = ''
    for old_element in old_array:
        if old_element not in new_array:
            missing_element = old_element
            break

    return missing_element


if __name__ == '__main__':
    original_array = [1, 2, 3, 4, 5, 6]

    array1 = [7, 5, 6, 1, 4, 2]
    array2 = [5, 3, 1, 2]

    answer1 = find_missing_element(original_array, array1)
    print("Missing number:", answer1)

    answer2 = find_missing_element(original_array, array2)
    print("Missing number:", answer2)
