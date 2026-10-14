class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

        for i in t:
            if i in cache:
                if cache[i] > 0:
                    cache[i] -= 1
                else:
                    return False
            else:
                return False

        return True