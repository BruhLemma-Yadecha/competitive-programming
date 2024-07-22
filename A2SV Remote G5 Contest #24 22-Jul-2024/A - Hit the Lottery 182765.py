# Problem: A - Hit the Lottery - https://codeforces.com/gym/536373/problem/A

n = int(input())

denominations = [100, 20, 10, 5, 1]

bills = 0
for d in denominations:
    local_bills = n // d
    bills += local_bills
    n -= d * local_bills
    
print(bills)