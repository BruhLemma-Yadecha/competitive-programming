people = int(input())
responses = input().split()
easy = True
for response in responses:
    if response == '1':
        easy = False
        break
if easy:
    print("EASY")
else:
    print("HARD")