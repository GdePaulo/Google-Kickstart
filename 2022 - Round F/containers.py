# X Algorithm specified bidirectionality of edges
# ! Make sure the initial vertex is included in visited
# ! Read problem correctly, it goes bottom-up. You can just start from the bottom
# and then loop through all descendents row by row, since you know the next
# row will be 1 + the level of the current row
# X MOST IMPORTANT OF ALL!!!!!! Was using list to check if visited, but
# look up is super slow O(n). When using set it is O(1). Could'Ve gotten 15 points.
def run_solution(n, q, connections, queries):
    # print(connections)
    adjacency_list = {1:[]}
    levels = {1:1}

    level_amounts = {1:1}
    # Complete bidirectional
    for i, j in connections:
        if i in adjacency_list:
            adjacency_list[i].append(j)
        else:
            adjacency_list[i] = [j]
        
        if j in adjacency_list:
            adjacency_list[j].append(i)
        else:
            adjacency_list[j] = [i]

    visited = {1}
    to_visit = [1]


    while to_visit:
        current = to_visit.pop()
        
        # print("current", current)
        for neighbor in adjacency_list.get(current, []):
            # print("is",neighbor,"in",visited, neighbor in visited)
            if neighbor in visited:
                continue
            neighbor_level = levels[current] + 1
            levels[neighbor] = neighbor_level
            level_amounts[neighbor_level] = level_amounts.get(neighbor_level, 0) + 1
            # print("neigh", neighbor, "amounts", level_amounts)
            visited.add(neighbor)
            to_visit.append(neighbor)
    
    total_water = len(queries)
    containers_filled = 0
    # print(level_amounts)
    for i in range(1, len(level_amounts)+1):
        amount = level_amounts[i]
        # print("comparing", amount, total_water)
        if amount <= total_water:
            containers_filled += amount
            total_water -= amount
        else:
            return containers_filled


    # print(adjacency_list, levels, level_amounts)
    return containers_filled
        

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):

    n, q = map(int, input().split())
    
    connections = []
    for c in range(0, n-1):
        i, j = map(int, input().split())
        connections.append((i, j))
    queries = []
    for c in range(0, q):
        query = int(input())
        queries.append(query)
        
    result = run_solution(n, q, connections, queries)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
