t = int(input())

exes = []

for _ in range(t):
    ex_input = input()
    exes.append(ex_input)

for ex in exes:
    main_stack = []
    res_stack = []
    
    for i in ex:
        main_stack.append(i)

        if i.isalpha(): # Add to res_stack if i is an operand (alphabetical letter)
            res_stack.append(i)
        
        if i == ")": # Unpack operators to res_stack from current bracket in main_stack when encountering a closed paranthese
            for j in range(len(main_stack)-1,-1,-1):
                if main_stack[j] in "+-*/^":
                    res_stack.append(main_stack[j])
                
                if main_stack[j] == "(":
                    main_stack.pop()
                    break

                main_stack.pop()

    for x in res_stack:
        print(x,end='')
    
    print()

'''
Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''