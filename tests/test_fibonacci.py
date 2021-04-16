from src.algorithms.fibonacci import fib

def test_fibbonacci_initial_0():
  res = fib(0)
  assert res == 0

def test_fibbonacci_initial_1():
  res = fib(1)
  assert res == 1

def test_fibbonacci_2():
  res = fib(2)
  assert res == 1

def test_fibbonacci_55():
  res = fib(10)
  assert res == 55