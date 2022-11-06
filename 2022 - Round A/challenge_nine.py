
def run_solution(n):
    string_number = str(n)
    candidates = []
    for digit in range(0, 10):
        string_digit = str(digit)
        for i in range(len(string_number) + 1):
            if digit == 0 and i==0:
                continue
            test_concatenation = string_number[:i] + string_digit
            if i < len(string_number):
                test_concatenation += string_number[i:]
            
            if int(test_concatenation)%9==0:
                candidates.append(int(test_concatenation))
    candidates.sort()
    return candidates[0]    
        
    

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    n = input()

    result = run_solution(n)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
