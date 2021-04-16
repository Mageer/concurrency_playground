from performance.performance import benchmark
from algorithms.fibonacci import fib

num = 5
(fib_num, duration) = benchmark(fib, 33)

print(f"Fib number for {num} is: {fib_num}")
print(f"Duration: {duration}")
