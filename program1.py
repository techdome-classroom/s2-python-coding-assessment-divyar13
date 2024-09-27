class Solution(object):
  #  def isValid(self, s):
  #      """
   #     :type s: str
  #      :rtype: bool
 #       """
   #     pass

 def isValid(s: str) -> bool:
    
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop the top element from the stack if not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all the brackets were properly closed
    return not stack





    



  

