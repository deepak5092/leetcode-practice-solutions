class Solution:
    def isValid(self, s: str) -> bool:
       stack = [] 
       mapChars = {")":"(", "}":"{", "]":"["}

       for ch in s:
            print(ch)
            if ch not in mapChars:
                stack.append(ch)
            else:
                if stack and stack[-1] == mapChars[ch]:
                    stack.pop()
                else:
                    return False

       return len(stack) == 0