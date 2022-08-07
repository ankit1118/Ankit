class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        cnt = collections.Counter(s)
        for ch in s:
            if ch not in stack:
                while stack and ch <= stack[-1] and cnt[stack[-1]] > 1:
                    cnt[stack.pop()] -=1
                stack.append(ch)
            else:
                cnt[ch] -=1
        return "".join(stack)