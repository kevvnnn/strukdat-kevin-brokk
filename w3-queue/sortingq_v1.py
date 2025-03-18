x, stop = map(int, input().split())
queue = []
stack1 = []
stack2 = []

# Take inputs and place into queue
stop_flag = 0
for i in range(x):
    num = int(input())
    if num == stop:
        stop_flag += 1
    if stop_flag == 0:
        queue.append(num)

# Move nums from queue to stack1
for _ in range(len(queue)):
    num = queue.pop(0)
    stack1.append(num)

min_value = float('inf')
while stack1 or stack2:
    # Finding the min (done while moving numbers from stack1 to stack2)
    while stack1:
        num = stack1.pop()
        stack2.append(num) # Moves all nums to stack2
        if num < min_value: # While moving, if a num is < current min, set that num as min
            min_value = num

    # Extracting the min (done while moving numbers from stack2 to stack1)
    while stack2:
        num = stack2.pop()
        if num == min_value: # If num = min, move to queue
            queue.append(num)
        else:
            stack1.append(num) # Returns remaining numbers to stack1 for next iteration
    
    min_value = float('inf') # Resets the min after the latest min has been moved to queue

    print(f'q: {queue}')
    print(f'1: {stack1}')
    print(f'2: {stack2}')

print(*queue)

'''Input
10 5
7
3
8
1
2
4
6
2
5
1

Output:
3 7 8
1 2 2 3 4 6 7 8'''