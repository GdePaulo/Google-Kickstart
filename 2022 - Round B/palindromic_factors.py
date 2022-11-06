from math import floor, pi

def run_solution(a):
    palindrome_amount = 0
    # for i in range(1, a+1):
    #     if a % i == 0:
    
    for factor in factors(a):
        test_number = str(factor)
        if test_number == test_number[::-1]:
            palindrome_amount += 1
    return palindrome_amount
    
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    a = int(input())

    result = run_solution(a)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
