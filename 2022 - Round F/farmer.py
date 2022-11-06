# ! 
def run_solution(d, n, x, plants):
    highest_value_plants = sorted(plants, key= lambda s:s[2]/s[1], reverse=True)
    current_best_type = 0
    reward = 0
    
    for i in range(0, d):
        energy_left = x
        days_left = d - i
        while energy_left > 0:
            chosen_plant = highest_value_plants[current_best_type]

            while chosen_plant[0] == 0 or chosen_plant[1] > days_left:
                current_best_type += 1
                if current_best_type >= len(highest_value_plants):
                    return reward
                chosen_plant = highest_value_plants[current_best_type]            
            print("I chose", chosen_plant)
            if energy_left >= chosen_plant[0]:
                reward += chosen_plant[2] * chosen_plant[0]
                energy_left -= chosen_plant[0]
                highest_value_plants[current_best_type] = (0, chosen_plant[1], chosen_plant[2])
            else:
                reward += chosen_plant[2] * energy_left
                highest_value_plants[current_best_type] = (chosen_plant[0] - energy_left, chosen_plant[1], chosen_plant[2])
                energy_left = 0
    return reward


        

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
