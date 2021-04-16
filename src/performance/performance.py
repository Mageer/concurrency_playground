import time 

def benchmark(func, num):
  start_time = time.time()
  res = func(num)
  duration = time.time() - start_time
  return (res, duration)
