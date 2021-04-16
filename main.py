import performance as P
import fibonacci as F

p = P.Performance()
s = F.Solver()
num = 5

(fib_num, duration) = p.time(s.fib, 32)

res_msg = 'Fib number for {num} is: {fib_num}'.format(num=num, fib_num=fib_num)
duration_msg = 'Duration: {duration}'.format(duration=duration)

print(res_msg)
print(duration_msg)