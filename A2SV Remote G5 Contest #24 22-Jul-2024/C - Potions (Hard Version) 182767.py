# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

n = int(input())
potions = list(map(int, input().split()))

# should always take potions that increase health (track poison?)
# running sum of health?
# essentially can tank some potions if needed
# order makes it tricky
taken = 0
health = 0
poisons = []
for potion in potions:
    if potion < 0: # we will never be in a scenario where we need to remove a health boosting potion
        heapq.heappush(poisons, potion)
    if health + potion < 0:
        # remove a potion picked up before?
        health += -heapq.heappop(poisons) # recover health from worst seen yet
        taken -= 1 # swap so
    health += potion
    taken += 1
print(taken)