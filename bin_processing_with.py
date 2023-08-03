import random
from timeit import default_timer as timer
import numpy
from multiprocessing import Process
from multiprocessing import Pool

array = numpy.sort(numpy.random.uniform(-100000, 100000, size=1000000))

counter = 1


def bin_search(arr: [int], num: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        guess = arr[(low + high) // 2]
        if guess == num:
            return (low + high) // 2
        elif guess < num:
            low = (low + high) // 2 + 1
        else:
            high = (low + high) // 2 - 1
    return None


def foo() -> None:
    num = array[random.randint(0, len(array) - 1)]
    res = bin_search(array, num)
    # print(f"TEST {counter}")
    # print(f"searching for {num}\nresult = {res}")
    # print()


def foo2() -> None:
    for i in range(375000):
        foo()


if __name__ == "__main__":
    procs = []

    start_time = timer()
    for i in range(8):
        proc = Process(target=foo2)
        procs.append(proc)
        proc.start()
        # counter += 1

    for proc in procs:
        proc.join()

    end_time = timer() - start_time

    print(f"--- {end_time} seconds ---")
