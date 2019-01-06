#!/home/anton/anaconda3/bin/python
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
import random

## Maximum size of data to test algorithm
N = 500
## Number of iterations when testing each size
ITERATIONS = 10

def plot_test_time_scatter_single(sizes, times):
    """Plots a scatter plot of data size and times using matplotlib

    Args:
        sizes (list): List of size x of numbers that represent a size
                      related to data used for testing
        times (list): List of size x of float or integer numbers that
                      represent a time related to data of size x
    """
    ## Setup size, color, and corresponding x & y coordinates
    area = np.pi * 3
    colors = (0,0,0) 
    x = np.array(sizes)
    y = np.array(times)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s = area, c = colors)

    ## Plot scatter plot of test time
    plt.show()
    
def plot_test_time_scatter_mult(sizes, times, colors=None):
    """Plots a scatter plot of data size and times of one or more data
    pairs. plot_test_time_scatter_single() is a specific case of this
    method.

    Args:
        sizes (list): List of size n*x that represent sizes related to
                      testing data
        times (list): List of size n*x that represent times related to
                      result of testing data
        colors (list): List of size n, with elements of type tuple that
                      are a hex representation of colors
    """
    if len(sizes)!=len(times) or len(times)!=len(colors) or len(colors)!=len(sizes):
            raise Exception("Length of all arguments must all be the same: len()")
                            
    ## Setup size of all coordinates
    area = np.pi * 3

    ## Set up colors
##    if colors is None:
##        colors = [(0,0,0) for i in range(len(sizes))]

    ## Convert list argument to numpy array for matplotlib compatibility
    x = np.array(sizes)
    y = np.array(times)

    fig, ax = plt.subplots()
    for i in range(len(sizes)):
        ax.scatter(x[i], y[i], s=area, c=colors[i])
    ## Plot scatter plot
    plt.show()

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
    
def test_algorithm_runtime(algorithm, min_input, max_input, iterations):
    """Implements an algorithm with data of various sizes to visualize
    algorithm's running time

    Args:
        algorithm (method): Algorithm in form of function with first param that
                            is list of data
        min_input (int): Minimum length of data used in the algorithm's test
        max_input (int): Maximum length of data used in the algorithm's test
        iterations (int): Number of repetitions for each size of data
    """

    test_sizes = [i for i in range(min_input, max_input+1)]
    test_times = []
    for i in range(min_input, max_input+1):
        test_list = [random.random() for j in range(i)]
        ## Repeat algorithm with one size "iterations" times to improve
        ## accurracy
        time_sum = 0
        for j in range(iterations):
            start_time = datetime.now()
            algorithm(test_list)
            time_sum+=((datetime.now() - start_time)*1e9).total_seconds()
        test_times.append(time_sum/iterations)

    ## Plot running time results w/ matplotlib
    plot_test_time_scatter_single(test_sizes, test_times)
    
if __name__ == "__main__":
    ##test_algorithm_runtime(shell_sort, 2, N, ITERATIONS)
    a = [random.randrange(1,100) for i in range(20)]
    print(merge_sort(a))
    
