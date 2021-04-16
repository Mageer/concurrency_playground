from src.performance.performance import benchmark
import time

def test_duration():
  seconds = 0.1
  (res, duration) = benchmark(lambda x: time.sleep(x), seconds)
  assert seconds - 0.01 <= duration <= seconds + 0.01

def test_res():
  val = 11
  (res, duration) = benchmark(lambda x: x, val)
  assert res == val