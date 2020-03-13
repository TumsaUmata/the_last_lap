class Solution:
    def isBalanced(self, s):
        balanced = True
        stack = []
        index = 0
        while index < len(s) and balanced:
            parenthesis = s[index]
            if parenthesis in "([{":
                stack.append(parenthesis)
            else:
                if not stack:
                    balanced = False
                else:
                    top = stack.pop()
                    if self.isMatched(top, parenthesis):
                        balanced = False
            index += 1

        if balanced and not stack:
            return "YES"
        else:
            return "NO"

    def isMatched(self, open, close):
        opening_parentheses = "([{"
        closing_parentheses = ")]}"
        return opening_parentheses.index(open) != closing_parentheses.index(close)


class Solution2:
    def isBalanced(self, s):
        """
        In this solution, we need to first initialize a mapping for each valid bracket combination.
        Then, we create a stack using a Python list.
        This is essentially the push and pop method.
        We add any opening bracket (booked_item.e., (, {, [) to the stack.
        Since we have a mapping of the corresponding closed bracket in the dictionary,
        we can use the last entered opening bracket in our stack to verify if the closing bracket is correct.

        If we bump into a closing bracket in the given string,
        then we go straight to our else statement and check if the stack is empty or not.
        If the stack is empty then we return False, meaning that we never bumped into an opening bracket,
        which is not valid (e.g., '}{').
        If there are opening brackets in the stack then we pop off the most recent opening bracket from the stack and
        check if the corresponding closed bracket matches the current closing bracket in our for loop iteration.
        If they do not match then we return False. For example, if we have a stack of [(,{] and our string is '({})',
        then we are essentially checking if '}' in the string matches the dictionary value of '{' which is '}'.
        This is true, so we keep going.

        In the end, the stack should be empty because it means we had a corresponding closing bracket
        for each opening bracket. We return False in the end if the stack is not empty because this means that
        we only had opening brackets, such as cases like '((('. I hope this helps.
        """
        stack = []
        parentheses_dict = {'{': '}', '[': ']', '(': ')'}
        for parenthesis in s:
            if parenthesis in "}])":
                if not stack or parentheses_dict[stack.pop()] != parenthesis:
                    return "NO"
            else:
                stack.append(parenthesis)

        return "NO" if stack else "YES"


class Solution3:
    def isBalanced(self, s):
        stack = []
        closing = [')', ']', '}']
        opening = ['(', '[', '{']

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if not stack:
                    return "NO"
                last = stack.pop()
                if opening.index(last) != closing.index(ch):
                    return "NO"
        return "NO" if stack else "YES"


class Solution4:
    def isBalanced(self, s):
        """O(n) Time Complexity and O(1) Space Complexity"""
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return "NO" if s else "YES"


if __name__ == '__main__':
    s = Solution4()
    print(s.isBalanced("{[()]}"))
    print(s.isBalanced("{[(])}"))
    print(s.isBalanced("{{[[(())]]}}"))
