def fill(n,q,g):
  #print("N", n, "Q", q)
  #print(g)
  # find number of nodes at each level
  levels = {}
  visited = set()
  curlevel = 0
  queue = [1]

  while len(queue) > 0:
    #print(queue)
    levels[curlevel] = len(queue)
    for i in range(len(queue)):
      visited.add(queue[i])
      for node in g[queue[i]]:
        if node not in visited:
          queue.append(node)
    queue = queue[levels[curlevel]:]
    curlevel += 1

  #print(levels)
  count = 0
  curlevel = 0
  curwater = 0.0
  for i in range(q):
    #print(curwater)
    curwater += 1.0 / levels[curlevel]
    if curwater >= 1.0:
      count += levels[curlevel]
      #print('CURWATER', curwater, 'COUNT', count)
      curlevel += 1
      curwater = 0.0

  return count

def run_solution(n, q, connections, queries_amount, adjacency_list):
    # print(connections)
    # adjacency_list = {1:[]}
    levels = {1:1}

    level_amounts = {1:1}

    print("Building adjacency list")

    # Complete bidirectional
    # for i, j in connections:
    #     if i in adjacency_list:
    #         adjacency_list[i].append(j)
    #     else:
    #         adjacency_list[i] = [j]
        
    #     if j in adjacency_list:
    #         adjacency_list[j].append(i)
    #     else:
    #         adjacency_list[j] = [i]

    visited = set()
    to_visit = [1]

    print("Doing BFS")

    # while to_visit:
    #     current = to_visit.pop()
    #     for neighbor in adjacency_list.get(current, []):
    #         # print("is",neighbor,"in",visited, neighbor in visited)
    #         if neighbor in visited:
    #             continue
    #         neighbor_level = levels[current] + 1
    #         levels[neighbor] = neighbor_level
    #         level_amounts[neighbor_level] = level_amounts.get(neighbor_level, 0) + 1
    #         # print("neigh", neighbor, "amounts", level_amounts)
    #         visited.append(neighbor)
    #         to_visit.append(neighbor)

    ### Attempt 2
    current_level = 0
    while to_visit:
        # current = to_visit.pop()
        new_to_visit = []
        current_level += 1
        level_amounts[current_level] = len(to_visit)
        for node in to_visit:
            visited.add(node)
            for neighbor in adjacency_list.get(node, []):
                # print("is",neighbor,"in",visited, neighbor in visited)
                if neighbor in visited:
                    continue
                # neighbor_level = levels[current] + 1
                # levels[neighbor] = neighbor_level
                # print("neigh", neighbor, "amounts", level_amounts)
                # visited.append(neighbor)
                new_to_visit.append(neighbor)
        to_visit = new_to_visit
        
    ### Try Authors
    
    # find number of nodes at each level
    # levels = {}
    # visited = set()
    # curlevel = 1
    # queue = [1]
    # while len(queue) > 0:
    #     #print(queue)
    #     levels[curlevel] = len(queue)
    #     for i in range(len(queue)):
    #         visited.add(queue[i])
    #         for node in adjacency_list[queue[i]]:
    #             if node not in visited:
    #                queue.append(node)
    #     queue = queue[levels[curlevel]:]
    #     curlevel += 1

    # level_amounts = levels
    print("Calculating containers filled")

    total_water = q
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
    
    print("Reading connections")
    connections = []

    adjacency_list = {}
    for j in range(n):
        adjacency_list[j+1] = []

    for c in range(0, n-1):
        i, j = map(int, input().split())
        # connections.append((i, j))

        if i in adjacency_list:
            adjacency_list[i].append(j)
        else:
            adjacency_list[i] = [j]
        
        if j in adjacency_list:
            adjacency_list[j].append(i)
        else:
            adjacency_list[j] = [i]

    queries = 0
    print("Reading queries")
    for c in range(0, q):
        # query = int(input())
        # queries.append(query)
        input()
        
    result = run_solution(n, q, connections, queries, adjacency_list)
    # result = fill(n, q, adjacency_list)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")

# Test 1 was perfect binary tree