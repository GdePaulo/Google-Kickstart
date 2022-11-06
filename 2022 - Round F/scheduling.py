import sys
#https://calvh.medium.com/how-to-pass-input-files-to-stdin-in-vscode-cb31cd7740b8
def run_solution(n, k, x, d, meetings):
    # X Read properly. It's not about amount of people who need counseling, but amount of meetings
    # Whether 2 or 5 people have to, it's the meetings that they have that matters, which can overlap
    minimum_cancellations = sys.maxsize
    # X This is not supposed to go until the end of the domain
    for i in range(0, d - x + 1):
        window = (i, i+x)
        # print(window)
        # print("Counting overlapping")
        overlapping_people, all_overlapping_people = amount_overlapping(window[0], window[1], meetings)
        people_available = n - overlapping_people
        cancellations_needed = getTotalCancellations(all_overlapping_people, k, people_available)
        if minimum_cancellations > cancellations_needed:
            # people_overlapping = all_overlapping_people
            minimum_cancellations = cancellations_needed
        # print("overlapping", people_overlapping)
    return minimum_cancellations
        

def getTotalCancellations(people_overlapping, k, people_available):
    most_annoying_people = {k: v for k, v in sorted(people_overlapping.items(), key=lambda item: item[1])}
    people_needed = k - people_available
    if people_needed <= 0:
        return 0

    total_cancellations = 0
    for k in list(most_annoying_people.keys())[:people_needed]:
        total_cancellations += most_annoying_people[k]
    return total_cancellations

def amount_overlapping(l_window, r_window, meetings):
    
    people_overlapping = {}
    amount_overlapping = 0

    for p, l, r in meetings:
        # print("checking", p, l, r, " against ", l_window, r_window)
        if (l <= l_window and r >= r_window) or (l >= l_window and r <= r_window) or (l >= l_window and l < r_window) or (l <= l_window and r > l_window):
        # if (l <= r_window and l_window <= r):
        
            # print("overlapping")
            people_overlapping[p] = people_overlapping.get(p, 0) + 1
            amount_overlapping += 1
    return len(people_overlapping), people_overlapping


if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):

    n, k, x, d = map(int, input().split())
    m = int(input())
    meetings = []
    for c in range(0, m):
        p, l, r = map(int, input().split())
        meetings.append((p, l, r))
        
    result = run_solution(n, k, x, d, meetings)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")

# Read properly. Minimum meetings that have to be rescheduled, not people.

# Test case for minimum overlapping is maximum amount of people
# 2 1 1 1
# 4
# 2 0 1
# 1 0 1
# 2 0 1
# 1 0 1
