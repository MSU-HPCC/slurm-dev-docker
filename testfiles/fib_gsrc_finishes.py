import time
def fib(n):
  if (n == 0):
    return 0
  if (n == 1):
    return 1;
  return fib(n-1) + fib(n-2)


for i in range(30):
  print("The Fibonacci value at %sth position is: %s" % (i,fib(i)))


time.sleep(10)
