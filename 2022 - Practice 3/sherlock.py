"""Starter Code for Sherlock and Watson Gym Secrets CC Problem"""

# Complete the count_pairs function
def count_pairs(a, b, n, k):
  pairs = 0
  # TODO: Add logic to count the number of pairs modulo 10^9+7 (1000000007)
  
  for s in range(1, n+1):
    for w in range(1, n+1):
      if s==w:
        continue
      if (s**a + w**b)%k==0:
        # print(s, w): Safe
        pairs+=1

  pairs = pairs % (10 ** 9 + 7)
  return pairs

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    a, b, n, k = map(int, input().split())

    print("Case #%d: %d" % (tc, count_pairs(a, b, n, k)))

    # LOOK AT MORE EFFICIENT SOLUTION WHEN YOU HAVE TIME
