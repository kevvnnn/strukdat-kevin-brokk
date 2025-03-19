text = input()
beiju_chars = ""
normal_chars = ""
temp = ""

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

print(beiju_chars + normal_chars)
