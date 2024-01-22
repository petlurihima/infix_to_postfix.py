operators=['+','-','*','/','^','(',')']
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infixtopostfix(expression):
    stack=[]
    output=''
    for char in expression:
        if char not in operators:
            output+=char
        elif char=='(':
            stack.append('(')
        elif char==')':
            while stack and stack[-1]!='(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[char]<=priority[stack[-1]]:
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()
    return output

a=input("Enter infix expression:")
print("Infix expression:",a)
print("Postfix expression:",infixtopostfix(a))
