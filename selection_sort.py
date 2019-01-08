#!/home/anton/anaconda3/bin/python

def smallest_elem_index(input_list):
    """Returns the index of the smallest number in the list

    Args:
        input_list (list): List of numbers which are at least of length 1
    Returns:
        min_index (int): Index of list containing the smallest element of list
    """
    if len(input_list) == 0:
        raise Exception("List must contain at least 1 element")
    
    min_index = 0 
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[min_index]:
            min_index = i
    return min_index

def selection_sort(input_list):
    """Implementation of Selection Sort which orders a list of numbers

    Args:
        input_list (list): List of integers/floats
    Returns:
        input_list (list): Sorted list in an ascending order
    """
    for i in range(len(input_list)-1):
        ## By slicing the list incrementally, swap first element with lowest
        ## element of sliced list
        temp_item = input_list[i]
        smallest_index = smallest_elem_index(input_list[i:])
        input_list[i] = input_list[smallest_index+i]
        input_list[smallest_index+i] = temp_item
    return input_list
    
if __name__ == "__main__":
    pass
    
