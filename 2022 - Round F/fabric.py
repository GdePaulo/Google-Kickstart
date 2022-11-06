
def run_solution(n, shirts):
    shirts = sorted(shirts, key= lambda s:s[2])
    shirts_color = sorted(shirts, key= lambda s:s[0])
    shirts_durability = sorted(shirts, key= lambda s:s[1])
    color_indices = {x:i for i, x in enumerate(shirts_color)}
    durability_indices = {x:i for i, x in enumerate(shirts_durability)}
        
    same_order = 0
    
    for shirt in shirts:
        if color_indices[shirt]==durability_indices[shirt]:
            same_order+=1

    return same_order
        

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):

    n = int(input())
    
    shirts = []
    for i in range(0, n):
        shirt = input().split()
        c, d, u = shirt[0], int(shirt[1]), int(shirt[2])
        shirts.append((c, d, u))
    result = run_solution(n, shirts)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
