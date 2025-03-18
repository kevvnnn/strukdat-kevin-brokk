queue = []
num_ops = int(input())

for _ in range(num_ops):
    op = input()
    
    if op[0] == "+":
        queue.append(op[1:])
    
    elif queue:
        queue.pop(0) # Assumes there are only + & - ops
    
    if not queue: # else isn't used since we are checking after the op is done
        print("Queue empty.")
    
    print(f'{len(queue)}: {queue}')