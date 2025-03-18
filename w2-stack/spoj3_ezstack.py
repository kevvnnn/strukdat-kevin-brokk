num_ops = int(input())
ops = []
stack = []

for _ in range(num_ops):
    ops.append(list(map(int, input().split())))

for op in ops:
    if op[0] == 1:
        stack.append(op[1])
    
    if op[0] == 2:
        stack.pop()
    
    if op[0] == 3:
        if not stack:
            print("Empty!")
        else:
            print(stack[-1])