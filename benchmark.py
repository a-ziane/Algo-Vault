import time

def benchmark(algorithm, arr):
    start = time.time()
    sorted_arr = algorithm.sort(arr)
    end = time.time()
    elapsed = (end - start) * 1000  
    return sorted_arr, elapsed