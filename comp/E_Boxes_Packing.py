box_count = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
i = len(boxes) - 1
counter = 0
if len(boxes) == 1:
    print(1)
else:
    while len(boxes) > 0:
        if len(boxes) == 1:
            counter += 1
            break
        # loop through the boxes that are smaller and collect unique copies
        i = 0
        j = 1
        while j < len(boxes):
            if boxes[i] < boxes[j]:
                boxes[i] = 0
                i = j
            j += 1
        boxes[i] = 0
        counter += 1
        boxes = [x for x in boxes if x != 0] # remove all emptied boxes
print(counter)

