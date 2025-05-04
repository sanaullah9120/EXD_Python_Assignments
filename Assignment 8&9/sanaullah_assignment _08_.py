# Assignment -08 : Valid Parenthesis
def is_valid_parenthesis(string):
    """This function Checks if a string of parenthesis is valid. Args, is string :the input string contains a string of parenthesis.
    Returns:
    True if the string is valid ,otherwise False."""

    #-1 create a stack to store open parenthesis.stack is empty list used as temporary basket(stack) to keep open parenthesis untill match with closing one. 
    stack = []
    #-2 create a dictionary to map closing parenthesis to corresponding their opening parenthesis 
    mapping = {")":"(","}":"{","]":"["}
    #-3 Iterate through string,character by character
    for char in string:
        if char in "({[":   #-4 if the character is an opening parenthesis ,push it into stack.
            stack.append(char) 
        elif char in ")}]":  #-5 if the character is closing parenthesis
            #-6 if the stack is empty meaning no corresponing opening parenthesis or the top of stack doesn't match the opening parenthesis 
            # with this closing one,the string is invalid.

            if not stack or stack[-1] != mapping[char]:  # "not stack" means if the stack is empty & 'stack[-1]' means, is the top of the stack
                                                        # - matching with the current close bracket?
                return False                           #- if did not match,'invalid' and return 'False'
            #-7 Otherwise, pop the matching opening parenthesis from the stack
            stack.pop()                               #-if matche,then pop that parenthesis from stack
        #-8 After processing the entire string ,if the stack is empty ,it means all parenthesis were correctly matched and closed.
        # if the stack is not empty,some opening parenthesis were left unclosed,making the string invalid.
        
    return not stack #- 'not stack' means: is stack empty or not .if stack is empty,its means all opening brackets match accurately with closing once, 
                     #-so that function return 'True',if not stack is not empty its means some brackets remains unmatched,and return Fasle.

# Example usage of string and then calling function upon that strings
string1 = "()"
string2 = "(){}[]"
string3 = "(]"
string4 = "([)]"
string5 = "({[]})"

# calling a function and print result
print(f"'{string1}' is valid:{is_valid_parenthesis(string1)}")
print(f"'{string2}' is valid:{is_valid_parenthesis(string2)}")
print(f"'{string3}' is valid:{is_valid_parenthesis(string3)}")
print(f"'{string4}' is valid:{is_valid_parenthesis(string4)}")
print(f"'{string5}' is valid:{is_valid_parenthesis(string5)}")
        
            