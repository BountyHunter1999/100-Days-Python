with open("file1.txt") as f:
    f1 = f.readlines()
    # f1 = [int(x) for x in f1]

with open("file2.txt") as f:
    f2 = f.readlines()
    # f2 = [int(x) for x in f2]

result = [int(i) for i in f1 if i in f2]
print(result)
