lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

result = 0
passengers = 0
for i in range(1, len(lines)):
    line_values = lines[i].split(" ")
    added = int(line_values[0])
    removed = int(line_values[1])
    passengers += added - removed
    if passengers < 0:
        passengers = 0
    result = max(result, passengers)
print(result)
