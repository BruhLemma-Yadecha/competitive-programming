n, x = map(int, input().split())
position_modifier = list(map(int, input().split()))
bounces = 0
position = 0
while bounces < n and position <= x:
    position += position_modifier[bounces]
    bounces += 1
if position <= x:
    bounces += 1
print(bounces)