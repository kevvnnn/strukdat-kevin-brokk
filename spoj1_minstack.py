num_ops = int(input())
ops = []
main_stack = []
min_stack = []

for _ in range(num_ops):
    ops.append(list(input().split()))

for op in ops:
    if op[0] == "PUSH":
        main_stack.append(int(op[1])) # Append to main_stack
        if not min_stack or int(op[1]) < min_stack[-1]:
            # If min_stack is empty or the number to be appended is smaller than top of min_stack,
            min_stack.append(int(op[1])) # append immediately to min_stack
    
    if op[0] == "POP":
        if not main_stack: # If main_stack is empty
            print("EMPTY")
        if main_stack[-1] == min_stack[-1]: # If the top of both stacks match,
            min_stack.pop() # remove from min_stack
        main_stack.pop() # then remove from main_stack
        
    if op[0] == "MIN":
        if not min_stack: # If min_stack is empty
            print("EMPTY")
        print(min_stack[-1]) # Print top of min_stack
    
    # print("main:", main_stack)
    # print("min:", min_stack)