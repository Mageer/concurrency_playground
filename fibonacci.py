class Solver:
  def __init__(self):
    self.iteration = 0

  def fib(self, num: int):
    self.iteration += 1
    if num < 1: return 0
    if num == 1: return 1
    return self.fib(num-1) + self.fib(num-2)