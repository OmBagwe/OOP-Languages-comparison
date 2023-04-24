#benchmark_memory.py
import sys
import json

def measure_memory_usage():
    lst = [i for i in range(1000000)]
    memory_used = sys.getsizeof(lst)
    return memory_used

if __name__ == "__main__":
    result = {"memory_used": measure_memory_usage()}
    print(json.dumps(result))
