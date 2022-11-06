# RECURSION TOO EXPENSIVE, RUNTIME ERROR
def run_solution(r, c, adjacency):
    result = hamCycle(adjacency)
    if not result:
        result = "IMPOSSIBLE"
    else:
        result = "".join(result)
    return result


def isSafe(v, pos, path, adjacency):
    # Check if current vertex and last vertex
    # in path are adjacent
    if path[pos-1] not in adjacency[v]:
        return False

    # Check if current vertex not already in path
    if v in path:
        return False

    return True

# A recursive utility function to solve
# hamiltonian cycle problem
def hamCycleUtil(path, pos, adjacency):

    # base case: if all vertices are
    # included in the path
    if pos == len(adjacency):
        # Last vertex must be adjacent to the
        # first vertex in path to make a cycle
        if path[0] in adjacency[ path[pos-1] ]:
            return True
        else:
            return False

    # Try different vertices as a next candidate
    # in Hamiltonian Cycle. We don't try for 0 as
    # we included 0 as starting point in hamCycle()
    for v in list(adjacency.keys())[1:]:
        if isSafe(v, pos, path, adjacency):
            path[pos] = v
            if hamCycleUtil(path, pos+1, adjacency):
                return True

            # Remove current vertex if it doesn't
            # lead to a solution
            path[pos] = -1

    return False

def hamCycle(adjacency):
    path = [-1 for x in range(len(adjacency))]

    path[0] = (0, 0)

    if not hamCycleUtil(path,1, adjacency):
        # print ("Solution does not exist\n")
        return []
    path.append((0, 0))
    return getDirections(path)

def getDirections(path):
    
    # print(path)
    directions = []
    for i, (a, b) in enumerate(path[1:]):
        p_a, p_b = path[i]
        if a - p_a > 0:
            directions.append("S")
        elif a - p_a < 0:
            directions.append("N")
        elif b - p_b > 0:
            directions.append("E")
        else:
            directions.append("W")

    return directions


def encodeVertex(i, j, r):
    return i * r + j

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    r, c = map(int, input().split())
    adjacency = {}
    walkable = [[0 for _ in range(2 * c)] for _ in range(2 * r)]
    
    for i in range(0, r):
        columns = input()
        
        for j, s in enumerate(columns):
            can_walk = 1 if s == "*" else 0
            grid = [(2 * i, 2 * j), (2 * i + 1, 2 * j), (2 * i, 2 * j + 1), (2 * i + 1, 2 * j + 1)]
            
            for y, x in grid:
                walkable[y][x] = can_walk
    
    
    for i in range(0, 2*r):
        for j in range(0, 2*c):
            if walkable[i][j]:
                neighbors = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
                
                for y, x in neighbors:
                    if y >= 0 and y < 2*r and x >= 0 and x < 2*c:
                        # print((y, x))
                        if walkable[y][x]:
                            # ! Should not be set of sets, because tuple order matters
                            if (i, j) in adjacency:
                                adjacency[(i, j)].add( (y, x) )
                            else:
                                # ! Need to wrap in brackets because it interprets as iterable otherwise
                                adjacency[(i, j)] = set([(y, x)])

    
    # print(walkable)
    # print(adjacency)
    result = run_solution(r, c, adjacency)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
