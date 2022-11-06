# Cool things: - only allowed to go down - reimagines the problem is backwards outside going in
# - using recursive probing iterations - Dynamic programming
memory = {}
def run_solution(n, d, locks):
    global memory
    memory = {}
    return solve(0, n-1, 0, d, locks)


def solve(i, j, k, d, locks):
    global memory
    if (i, j, k) in memory:
        return memory[(i, j, k)]
    if i > j:
        memory[(i, j, k)] = 0
        return 0
    current_i = (locks[i] - k + d) % d
    current_j = (locks[j] - k + d) % d
    
    # i+1,j,(k−(D−currentVali)+D)modD)
    # this is a formula to basically go up. You are subtracting some steps from 
    # the amount you're going down (aka  we are going up) And then the +D mod D is to 
    # force it to be positive
    if current_i == 0 and current_j == 0:
        memory[(i, j, k)] = solve(i+1, j-1, k, d, locks)
    elif current_i == 0 and current_j > 0:
        memory[(i, j, k)] = solve(i+1, j, k, d, locks)
    elif current_i > 0 and current_j == 0:
        memory[(i, j, k)] = solve(i, j-1, k, d, locks)
    elif current_i > 0 and current_j > 0:
        i_steps_going_down = current_i
        i_steps_going_down_k = (k+current_i) % d
        i_steps_going_up = d - current_i
        i_steps_going_up_k = (k - (i_steps_going_up) + d) % d
        
        i_cost_going_down = i_steps_going_down + solve(i+1, j, i_steps_going_down_k, d, locks)
        i_cost_going_up = i_steps_going_up + solve(i+1, j, i_steps_going_up_k, d, locks)
        
        j_steps_going_down = current_j
        j_steps_going_down_k = (k+current_j) % d
        j_steps_going_up = d - current_j
        j_steps_going_up_k = (k - (j_steps_going_up) + d) % d

        j_cost_going_down = j_steps_going_down + solve(i, j-1, j_steps_going_down_k, d, locks)
        j_cost_going_up = j_steps_going_up + solve(i, j-1, j_steps_going_up_k, d, locks)
        memory[(i, j, k)] = min(min(i_cost_going_down, i_cost_going_up), min(j_cost_going_down, j_cost_going_up))
    return memory[(i, j, k)]

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    n, d = map(int, input().split())
    locks = list(map(int, input().split()))

    result = run_solution(n, d, locks)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
