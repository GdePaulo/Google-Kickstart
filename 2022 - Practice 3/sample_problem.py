
from re import M


def runSample():
    number_cases = int(input())
    print("i'm here")
    for i in range(0, number_cases):
        n, m = map(int, input().split())
        bag_values = map(int, input().split())
        total_value = sum(bag_values)
        remaining_candy = total_value % m
        print(f"Case #{i+1}: {remaining_candy}")

if __name__ == "__main__":
    runSample()