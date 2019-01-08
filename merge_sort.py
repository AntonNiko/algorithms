#!/home/anton/anaconda3/bin/python

def merge_sorted_lists(list1, list2):
    """Returns a list that is the merged version of 2 sorted lists
    provided as arguments

    Args:
        list1 (list): Sorted list of numbers
        list2 (list): Sorted list of numbers
    Returns:
        list1 (list): Sorted, merged version of the 2 lists
    """
    for j in range(len(list2)):
        for i in range(len(list1)):
            if list2[j] < list1[i]:
                list1.insert(i,list2[j])
                break
        ## If element cannot be sorted anywhere inside the list, means
        ## that it is greater than all elements. In that case, append to
        ## list
        if i==(len(list1)-1):
            list1.append(list2[j])
    return list1

def merge_sort(input_list):
    """Implements the merge sort algorithm to sort a list of numbers. Calls
    itself in a recursive manner with smaller and smaller slices of the lists
    until it can compare values of list of 2 elements
    
    Args:
        input_list (list): A list of numbers that may or may not be ordered
    Returns:
        list_sorted (list): The sorted list of numbers
    """
    length = len(input_list)
    if length == 2:
        if input_list[0] > input_list[1]:
            temp = input_list[1]
            input_list[1] = input_list[0]
            input_list[0] = temp
        return input_list
    elif length == 1:
        return input_list
    elif length == 0:
        raise Exception("Length of list must be at least 1")
    else:
        left_sorted = merge_sort(input_list[0:int(length/2)])
        right_sorted = merge_sort(input_list[int(length/2):])
        list_sorted = merge_sorted_lists(left_sorted, right_sorted)
        return list_sorted
    
if __name__ == "__main__":
    pass
    
