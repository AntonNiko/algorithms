#!/home/anton/anaconda3/bin/python
import random
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
import numpy as np
from datetime import datetime

N = 200
ITERATIONS = 10


def plot_test_time_scatter(sizes, times):
    rx, ry = 0.5, 0.5
    area = 0.5 * 0.5 * np.pi
    theta = np.arange(0, 2 * np.pi + 0.01, 0.1)
    
    area = np.pi * 3
    colors = (0,0,0) 
    x = np.array(sizes)
    y = np.array(times)
    fig, ax = plt.subplots()
    ax.scatter(x, y, s = area, c = colors)

    plt.show()

def smallest_elem_index(input_list):
    if len(input_list) == 0:
        raise Exception("List must contain at least 1 element")
    
    min_index = 0 
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[min_index]:
            min_index = i
    return min_index

def selection_sort(input_list):
    for i in range(len(input_list)-1):
        temp_item = input_list[i]
        smallest_index = smallest_elem_index(input_list[i:])
        input_list[i] = input_list[smallest_index+i]
        input_list[smallest_index+i] = temp_item
    return input_list
    
def test_algorithm_runtime(algorithm, min_input, max_input, iterations):
    test_sizes = [i for i in range(min_input, max_input+1)]
    test_times = []
    for i in range(min_input, max_input+1):
        test_list = [random.random() for j in range(i)]

        ## Repeat algorithm with one size to improve accuracy
        time_sum = 0
        for j in range(iterations):
            start_time = datetime.now()
            algorithm(test_list)
            time_sum+=((datetime.now() - start_time)*1e9).total_seconds()
        test_times.append(time_sum/iterations)

    plot_test_time_scatter(test_sizes, test_times)

def main():
    pass
    
if __name__ == "__main__":
    test_algorithm_runtime(selection_sort, 1, N, ITERATIONS)
