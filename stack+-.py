stack = []
num_ops = int(input())

for _ in range(num_ops):
    op = input()

    if op[0] == "+":
        stack.append(op[1:])
    
    elif stack:
        stack.pop() # Assumes there are only + & - ops
    
    if not stack: # else isn't used since we are checking after the op is done
        print("Stack empty.")

    print(f'{len(stack)}: {stack}')