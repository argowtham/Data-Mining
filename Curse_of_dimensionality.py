import random
import numpy
import itertools
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("==================================================")
    print("Program to demonstrate the curse of dimensionality")
    print("==================================================\n")
    # Generating n data points
    n = int(input("Enter the number of data points to be generated\n"))
    for l in range(0, 2):
        data_array = []
        data_point = []
        r_array, distance = [], []
        for k in range(1, 100):
            for i in range(0, n):
                for j in range(0, k):
                    data_point.append(random.random())  # Generating a data point as per the dimensionality required
                data_array.append(numpy.asarray(data_point))    # Appending all the data points created to a data array
                data_point = []
            data_list_array = numpy.asarray(data_array)
            distance = [numpy.linalg.norm(a-b) for a, b in itertools.combinations(data_list_array, 2)]
            data_array = []
            dmax = max(distance)
            dmin = min(distance)
            r_array.append(numpy.log10((dmax - dmin)/dmin))
        plt.plot(r_array)
        plt.ylabel("r(k) as a function of k")
        plt.legend(["100 data points", "1000 data points"])
        n *= 10
        print("Increasing n by 10 folds. New n = ", n)
    plt.show()

