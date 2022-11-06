Use with bash
cat ts1_input.txt | python farmer_new.py > output_farmer.txt
python farmer_new.py file ts1_input.txt



Round A 2022:
look more into challenge nine, palindrome and speed typing

Pay attention to test case constraints:

Round F 2022
Farmer: Test 1 was only 1 seed a day, Containers: Test 1 was perfect binary tree

Use appropriate data structure:

Round F 2022 containers: missed out on fifteen points and time because I used
a list instead of a set to check if vertex was in visited

Reimagine problem:

Round B 2022 padlock: starting from small and growing big is the same as starting from big and going small

Todo:
Investigate shylock.py solution
Farmer: Try to figure out why my brute force approach is to slow even with memoization and how to optimize.
! also be careful with global variables reuse during memoization
Implement further optimization for Test 3
Scheduling: optimize it further for test 2
Padlock: Further optimization for test 3
Hamiltonian tour: try rewriting Algorithm to not use recursion and do test 2



Binary Tree:
perfect tree height: h = log(N+1) - 1
nodes at each level = Ci = 2^(i-1)

Have breadth first search ready

Max heap

Dynamic Programming:
https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0