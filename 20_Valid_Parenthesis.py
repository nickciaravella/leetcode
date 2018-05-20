# https://leetcode.com/problems/valid-parentheses/description/
# Easy

def is_valid(s):
    characters = []    
    for char in s:
        if char in ['{', '[', '(']:
            characters.append(char)
            continue
        if len(characters) == 0:
            return False
        
        end_char = characters.pop()
        
        # Nice approach is to replace this comparison with a dictionary.
        if (end_char == '{' and char != '}') or \
           (end_char == '(' and char != ')') or \
           (end_char == '[' and char != ']'): 
           return False

    return len(characters) == 0
