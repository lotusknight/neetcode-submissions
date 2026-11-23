class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 1
        left = 0
        char_dict = {}
        for right, num in enumerate(s):
            if num in char_dict and char_dict[num] >= left:
                left = char_dict[num]+1
            char_dict[num] = right
            max_len = max(max_len, right-left+1)
        return max_len
            
