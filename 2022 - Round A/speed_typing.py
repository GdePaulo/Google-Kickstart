
def run_solution(i, p):
    if i==p:
        return 0
    if len(p) <= len(i):
        return "IMPOSSIBLE"

    # if any(x != i[0] for x in p):
    original_p = 0
    builder_p = 0
    deleted = 0
    for j in range(0, len(p)):
        original_letter = i[original_p]
        builder_letter = p[j]
        if original_letter == builder_letter:
            original_p +=1
            if original_p == len(i):
                deleted+= len(p) - j - 1
                break
        else:
            deleted+=1
    if original_p==len(i):
        return deleted
    else:
        return "IMPOSSIBLE"
    
        
    

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    i = input()
    p = input()

    result = run_solution(i, p)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
