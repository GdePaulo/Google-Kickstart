# ! read the constraints of the test cases, such as the first one only having one planting per day
# https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0
from heapq import heappop, heappush, heapify

def run_solution(d, n, x, plants):
    plants = [(q, l, v, i) for i, (q, l, v) in enumerate(plants)]
    seeds_left = [q for (q, l, v, i) in plants]
    easiest_plants = sorted(plants, key= lambda s:s[1])
    current_easiest_plant = 0

    # Creating empty heap
    heap = []
    heapify(heap)
    
    # Adding items to the heap using heappush
    # function by multiplying them with -1
    current_reward = 0
    
    for day in reversed(range(1, d + 1)):
        days_left = d - day

        
        while current_easiest_plant < len(easiest_plants) and easiest_plants[current_easiest_plant][1] <= days_left:
            easiest_plant = easiest_plants[current_easiest_plant]
            val, id = easiest_plant[2], easiest_plant[3]
            heappush(heap, (-val, id))
            current_easiest_plant += 1

        power_left = x
        daily_reward = 0

        while power_left > 0 and heap:
            best_plant_id = heap[0][1]
            b_q, b_l, b_v, b_i = plants[best_plant_id]
            seeds = seeds_left[b_i]

            if seeds >= power_left:
                seeds_left[b_i] -= power_left
                daily_reward += power_left * b_v
                power_left = 0
            else:
                power_left -= seeds_left[b_i]
                daily_reward += seeds_left[b_i] * b_v
                seeds_left[b_i] = 0
                heappop(heap)

        current_reward += daily_reward
    return current_reward

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
