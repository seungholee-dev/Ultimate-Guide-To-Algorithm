# Counting Sort --> For String
def counting_sort(arr):
    count_arr = [0 for _ in range(256)] # 256 for ASCII Strings

    # Count the elements
    for element in arr:
        count_arr[ord(element)] += 1

    # Precomputing the starting point
    before_sum = 0
    for i in range(len(count_arr) - 1):
        tmp = count_arr[i]
        count_arr[i] = before_sum
        before_sum += tmp

    # Above can be coded like below as well!
    
    # num_items_before = 0
    # for i, count in enumerate(counts):
    #     counts[i] = num_items_before
    #     num_items_before += count

    # Create output array
    output = ["" for _ in range(len(arr))]

    # Filling in the output array based on the count_arr
    for element in arr:
        char_id = ord(element)
        print_index = count_arr[char_id]
        output[print_index] = element
        
        count_arr[char_id] += 1

    return output

# Counting Sort that can also sort negative numbers
def better_counting_sort(arr):
    pass


if __name__ == "__main__":
    # arr = [8, 7, 0, 1, 2, 3, 8, 9, 4, 3, 4]
    # print(counting_sort(arr))

    arr = ["c", "d", "a", "u", "i", "g", "r", "a", "d", "b"]
    print(counting_sort(arr))

    # arr = [2, 1]
    

    arr = [1]
    # print(counting_sort(arr))


    # Advanced Counting Sort
