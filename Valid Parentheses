class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            # loop through to find the opening brackets, and add to the stack
            if char == "(" or char == "{" or char == "[":
                # add the opening brackets, to the stack
                stack.append(char)
            else:
                # if non of the open brackets are in the string, then return    false
                if not stack:
                    return False;
                
                # checks if the close bracket is matched with the open barcket in the stack. if yes, then pops off the top element 
                if char == ")" and stack[-1] == '(':
                    stack.pop()
                    print(stack, "1")
                elif char == "}" and stack[-1] == '{':
                    stack.pop()
                    print(stack)
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                    print(stack)
                else:
                    return False
        # stack empty = false -NOT - returns true. Stack not empty = true - Not - return false 
        return not stack
        """
        :type s: str
        :rtype: bool
        """

        # (), {}, []

        

        # correct order 


        #  closed bracket, has samed bracket and same type.
