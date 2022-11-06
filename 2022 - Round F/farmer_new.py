# ! read the constraints of the test cases, such as the first one only having one planting per day
# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0
memory = {}
def run_solution(d, n, x, plants):
    current_plants = set(range(len(plants)))
    result = recursive(d, n, x, plants, 1, current_plants)
    global memory
    memory = {}
    return result


def recursive(d, n, x, plants, current_day, current_plants):
    days_left = d - current_day
    if days_left == 0:
        return 0

    maximum_value = 0
    global memory

    for i, plant_i in enumerate(current_plants):
        (q, l, v) = plants[plant_i]
        if l <= days_left:
            new_plants = frozenset({x for j, x in enumerate(current_plants) if j!=i})
            next_day = current_day + 1
            
            # print((new_plants, next_day), " In memory?", memory)
            if (new_plants, next_day) in memory:
                
                # print("Yes")
                future_value = memory[(new_plants, next_day)]
            else:
                future_value = recursive(d, n, x, plants, current_day+1, new_plants)
                memory[(new_plants, next_day)] = future_value


            current_value = v + future_value
            if current_value > maximum_value:
                maximum_value = current_value
    return maximum_value


        

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):

    d, n, x = map(int, input().split())
    
    plants = []
    for i in range(0, n):
        q, l, v = map(int, input().split())
        plants.append((q, l, v))
        
    result = run_solution(d, n, x, plants)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
