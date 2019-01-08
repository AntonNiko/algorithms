#!/home/anton/anaconda3/bin/python

def sort_last_list_element(input_list):
    """Sorts the last element of a list into the rest of the last that is ordered
    in an ascending order

    Args:
        input_list (list): List of at least 2 elements, with all except the last
                           element being ordered in an ascending manner
    Returns:
        input_list (list): An ordered list of numbers in an ascending order
    """
    ## Method returns exception at line 73 if length is less than 2
    if len(input_list) < 2:
        raise Exception("List must contain at least 2 elements for sorting")
    
    temp = input_list[-1]
    for i in range(len(input_list)-2, -1, -1):
        if input_list[i] < temp or i==0:
            break
    for j in range(len(input_list)-1, i, -1):
        input_list[j] = input_list[j-1]

    if i==0 and input_list[0] > temp:
        input_list[i] = temp
    else:
        input_list[i+1] = temp
    return input_list

def insertion_sort(input_list):
    """Implementation of Insertion Sort which orders a list of numbers in
    ascending manner

    Args:
        input_list (list): List of numbers which can be distributed in any order
    Returns:
        input_list (list): Ordered list of numbers in an ascending manner

    """
    for i in range(1,len(input_list)):
        if input_list[i] < input_list[i-1]:
            ## If element is not in order, sort in the preceeding elements
            input_list[:i+1] = sort_last_list_element(input_list[:i+1])
    return input_list

def shell_sort(input_list):
    """Implementation of the Shell Sort algorithm to order a list of numbers

    Args:
        input_list (list): List of integers/floats
    Returns:
        input_list (list): Sorted list in an ascending order
    """
    h = int(len(input_list)/3)
    while True:
        if h<2:
            h = 1
            input_list = insertion_sort(input_list)
            break
        else:
            h_unsorted_list = input_list[::h]
            h_sorted_list = insertion_sort(h_unsorted_list)
            input_list[::h] = h_sorted_list
            h = int(h/3)
    return input_list
    
if __name__ == "__main__":
    pass
    
