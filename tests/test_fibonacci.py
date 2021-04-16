import sys
from src import fibonacci

def test_fibbonacci_initial_0():
  s = fibonacci.Solver()
  res = s.fib(0)
  assert res == 0

def test_fibbonacci_initial_1():
  s = fibonacci.Solver()
  res = s.fib(1)
  assert res == 1

def test_fibbonacci_2():
  s = fibonacci.Solver()
  res = s.fib(2)
  assert res == 1

def test_fibbonacci_55():
  s = fibonacci.Solver()
  res = s.fib(10)
  assert res == 55