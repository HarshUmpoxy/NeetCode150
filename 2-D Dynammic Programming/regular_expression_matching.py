# MUST CODE YOURSELF
# The catch is with '*', it can match 0 or more characters preceeding it
# So, we start iterating from the end. Also, there are three base conditions
# The one extra is for empty s and all * p edge case
# Also, skip * or skip the other char in s

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(i: int, j: int) -> bool: # i is string, j is pattern

            # both exhausted
            if i < 0 and j < 0:
                return True

            # pattern exhausted, string not
            elif i >= 0 and j < 0:
                return False

            # string exhausted, pattern not
            elif i < 0 and j >= 0:
                if p[j] == '*':
                    return match(i, j - 2)
                return False

            # current characters match or '.'
            if s[i] == p[j] or p[j] == '.':
                return match(i - 1, j - 1)

            # current pattern is '*'
            elif p[j] == '*':
                if p[j - 1] == s[i] or p[j - 1] == '.':
                    # one or more OR zero occurrences
                    return match(i - 1, j) or match(i, j - 2)
                else:
                    # zero occurrences only
                    return match(i, j - 2)

            else:
                return False

        return match(len(s) - 1, len(p) - 1)
