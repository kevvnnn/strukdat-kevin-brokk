text = input()
beiju_chars = [] # queue
# normal_chars = [] # queue
temp = [] # stack
# A deque should be a better implementation
# bracket_status = 0

for char in text:
    # When encountering a closing bracket, append all chars inside bracket to beiju_chars
    if char == "]": # Beware about brackets entering beiju/normal!
        for i in range(len(temp)-1,-1,-1):
            if temp[i] != "[":
                beiju_chars.append(temp.pop())
            elif temp[i] == "[":
                temp.pop()
                break # Ensures one loop of iterating over chars inside bracket per closing bracket encountered
    
    else:
        temp.append(char)
    
    print(temp)
    # Where to add normal_chars?

# print(*beiju_chars)
print(*temp)
# Now ur problem is to print them in the correct order

'''
for char in text:
    if char == "[":
        bracket_status += 1
        continue # Skips the following code for this iteration (avoids either [] being appended)
    elif char == "]":
        bracket_status -= 1
        continue # Same as above
    
    if bracket_status == 0: # Assume first encountered brackets are always "["
        normal_chars += char
    else:
        beiju_chars += char

print(beiju_chars + normal_chars)'''