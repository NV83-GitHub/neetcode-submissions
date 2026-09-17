class Solution:
    def isValid(self, s: str) -> bool:
        # Ok on a 2 part dans ce mécanisme.
        # Une reference que l'on va checker , un hashmap avec les paires de parenthèse
        # un loop qui pousse les char de la string dans un array stack. 
        # Lorsque la stack recoit des parenthèse ouvrante, elle les accèpte
        # Lorsqu'elle recoit un parenthèse fermente elle check si le précédent est l'autre de la paire
        # Si pas return false
        # Si oui pop() et push la c suivante. 
        # Si stack empty => valid => True
        brackets_hash = {"}": "{", "]": "[", ")": "("}
        stack = []

        for bracket in s:
            # check if opening or closing bracket
            if bracket in brackets_hash: # is found by key so is closing bracket
                if stack and stack[-1] == brackets_hash[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack