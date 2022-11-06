def number_of_record_breaking_days(number_of_days, vistors):
  record_breaking_days = 0
  # TODO: implement this method to return the number of record breaking days
  maximum_so_far = 0
  if number_of_days == 1:
    return 1
  
  
  for i in range(number_of_days-1):
    current_visitors = vistors[i]
    next_visitors = vistors[i+1]
    if i == 0 and current_visitors > next_visitors:
      record_breaking_days+=1
    elif current_visitors > next_visitors and current_visitors > maximum_so_far:
      record_breaking_days+=1
    if current_visitors > maximum_so_far:
      maximum_so_far = current_visitors
  
  if next_visitors > maximum_so_far:
    record_breaking_days+=1
    
  return record_breaking_days

def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1, 1):
    number_of_days = int(input())
    vistors = list(map(int, input().split()))

    ans = number_of_record_breaking_days(number_of_days, vistors)

    print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
  main()
