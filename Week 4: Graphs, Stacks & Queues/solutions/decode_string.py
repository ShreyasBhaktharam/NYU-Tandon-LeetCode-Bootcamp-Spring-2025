class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []
        curr = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr)
                num_stack.append(curr_num)
                curr = ""
                curr_num = 0
            elif c == ']':
                count = num_stack.pop()
                prev = stack.pop()
                curr = prev + curr * count  # Expand the repeated sequence
            else:
                curr += c

        return curr

# Example usage:
# sol = Solution()
# print(sol.decodeString("3[a2[c]]"))  # Output: "accaccacc"