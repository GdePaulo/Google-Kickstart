#1
#6
#101101

from itertools import product
from math import floor, pi
from tabnanny import check

def run_solution(r, a, b):
    total_radius = 0
    current_radius = r
    multiply = True
    while current_radius > 0:
        total_radius += pi * current_radius ** 2
        if multiply:
            current_radius *= a
        else:
            current_radius = floor(current_radius/b)
        multiply = not multiply
    return total_radius
    

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    r, a, b = map(int, input().split())

    result = run_solution(r, a, b)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
