# benchmark_efficiency.py
import time
import random
import json

def measure_efficiency():
    lst = [random.randint(1, 1000000) for _ in range(1000000)]
    start_time = time.time()
    sorted_list = sorted(lst)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    result = {"efficiency": measure_efficiency()}
    print(json.dumps(result))
