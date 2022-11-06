#1
#6
#101101

from itertools import product
from math import floor
from tabnanny import check

def run_solution(n, s):
    if n < 5:
        return "POSSIBLE"
    current_set = {""}
    
    for i in range(0, n):
        next_character = s[i]
        possible_characters = ["0", "1"] if s[i] == "?" else [s[i]]
        new_set = set()
        for prefix in current_set:
            for possible_character in possible_characters:
                with_new_character = prefix + possible_character

                if len(with_new_character) < 5:
                    is_palindrome = False
                else:
                    # is_palindrome = checkPalindrome(with_new_character[-5:], 5)
                    is_palindrome = with_new_character[-5:] == with_new_character[-5:][::-1]
                    
                    # print(with_new_character[-5:], with_new_character[-5:][::-1], is_palindrome)
                    if not is_palindrome:
                        # is_palindrome = checkPalindrome(with_new_character, 6)
                        is_palindrome = with_new_character == with_new_character[::-1]
                # print(i, prefix, with_new_character, is_palindrome)
                if not is_palindrome:
                    new_set.add(with_new_character[-5:])
                    # print("adding", with_new_character[-5:], new_set)
        current_set = new_set
        # print(current_set)
        if len(current_set) == 0:
            return "IMPOSSIBLE"
    return "POSSIBLE"    

def checkPalindrome(string, window_size):  
    if len(string) < window_size:
        return False
    has_palindrome = False
    for i in range(0, len(string) - window_size + 1):
        # !!! Typo was using wrong variable
        window = string[i:i+window_size]
        palindrome_in_window = True
        
        for j in range(0, floor(len(window)/2)):
            left = window[j]
            right = window[len(window)-j-1]
            
            if left != right:
                palindrome_in_window = False
                break
        # print(window, " has palindrome?", palindrome_in_window)
        if palindrome_in_window:
            return True
    return False
        

if __name__ == '__main__':
  # Read number of test cases
  num_cases = int(input())

  for tc in range(1, num_cases + 1):
    n = int(input())
    s = input()

    result = run_solution(n, s)
    # print("Case #%d: %d" % (tc, run_solution(i, p)))
    print(f"Case #{tc}: {result}")
