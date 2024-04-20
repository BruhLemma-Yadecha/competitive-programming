n, m = map(int, input().split())
dunes = list(map(int, input().split()))

i = 0
spice = 0
res = 0
sums = {0:1}
for dune in dunes:
    spice += dune
    remainder = spice % m
    if remainder in sums:
        res += sums[remainder]
    sums[remainder] = sums.get(remainder, 0) + 1
print(res)
