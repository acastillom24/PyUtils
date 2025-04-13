import time

def execution_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function {function.__name__} took {end - start:.4f} seconds to execute")
        return result
    return wrapper

@execution_time
def example():
    for i in range(10000000):
        i * 10000000
    return i

# Example usage:
if __name__ == "__main__":
    result = example()