# benchmark_processing_speed.py
import time
import json

def measure_processing_speed():
    start_time = time.time()
    result = 0
    for i in range(10000000):
        result += i
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    result = {"processing_speed": measure_processing_speed()}
    print(json.dumps(result))
