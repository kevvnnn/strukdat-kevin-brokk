while True:
    n = int(input())
    if n == 0:
        break
    
    trucks = list(map(int, input().split()))
    stack = []
    counter = 1 # Expected truck num
    print_flag = 0

    for truck in trucks:
        # Kalo Jeremy: dia pake while stack and stack[-1] == counter: pop (oke i use that)
        while stack and stack[-1] == counter:
            stack.pop()
            counter += 1

        # If current truck is in order
        if truck == counter:
            counter += 1 # Move to next expected truck
        
        # If stack has expected truck
        elif stack and stack[-1] == counter:
            stack.pop() # Pop from stack and
            counter += 1 # Move to next expected truck
        
        # If current truck is higher than top of stack = impossible
        elif stack and truck > stack[-1]:
            print_flag += 1
        
        # If current truck is not in order, push to stack
        else:
            stack.append(truck)
    
    if print_flag == 0:
        print("yes")
    else:
      print("no")

    '''
    Sample input:
    5
    5 1 2 4 3 
    0

    Sample output:
    yes'''

    '''
    Sample input star:
    10
    6 1 5 2 7 3 4 10 8 9
    0
    '''