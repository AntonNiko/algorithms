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
    pass
    
