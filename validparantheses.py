def isValid(s):
    pairs = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    stack = []
    ops = 0

    for i in s:
        if i in "({[":
            stack.append(i)
        
        if i in ")}]":
            if not stack:
                return False
            if stack[-1] == pairs[i]:
                stack.pop()
                ops += 1
            else:
                return False

    if not stack and ops != 0:
        return True
    else:
        return False

print(isValid("(){}}{"))