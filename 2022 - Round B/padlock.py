
def run_solution(n, d, locks):
    return solve(0, n-1, 0, d, locks)


def solve(i, j, k, d, locks):

    if i > j:
        return 0
    current_i = (locks[i] - k + d) % d
    current_j = (locks[j] - k + d) % d
    if current_i == 0 and current_j == 0:
        return solve(i+1, j-1, k, d, locks)
    elif current_i == 0 and current_j == 1:
        return solve(i+1, j, k, d, locks)
    elif current_i == 1 and current_j == 0:
        return solve(i, j-1, k, d, locks)
    elif current_i == 1 and current_j == 1:
        return 1 + solve(i+1, j-1, (k+1) % d, d, locks)

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    n, d = map(int, input().split())
    locks = list(map(int, input().split()))

    result = run_solution(n, d, locks)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
