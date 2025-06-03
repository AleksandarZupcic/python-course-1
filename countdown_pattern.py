'''
From the Loops category (Task #1 of 5):
Create a function countdown_pattern(n) that prints a countdown pattern like this:
If n = 5, the output should be:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

def countdown_pattern(n):
    for x in range(0, n + 1):
        for y in range(n, x, -1):
            print(f"{y - x} ", end = "")
        print()

n = 5
countdown_pattern(n)