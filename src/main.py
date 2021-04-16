import performance as P
import fibonacci as F

p = P.Performance()
s = F.Solver()
num = 5

(fib_num, duration) = p.time(s.fib, 33)

print(f"Fib number for {num} is: {fib_num}")
print(f"Duration: {duration}")
