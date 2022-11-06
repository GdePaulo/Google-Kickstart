from functools import reduce

def run_solution(a, b):
    interesting_integers = 0
    for i in range(a, b+1):
        digits = [int(x) for x in str(i)]

        summation = sum(digits)
        product = reduce(lambda a,b: a * b, digits, 1)

        if product % summation == 0:
            interesting_integers+=1

    return interesting_integers
        
    

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    a, b = map(int, input().split())

    result = run_solution(a, b)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
