class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        cur_max = 1
        left = 0
        num_pos = {}
        for i,num in enumerate(s):
            if num not in num_pos or num_pos[num] < left:
                num_pos[num] = i
                cur_len = i - left + 1
            else:
                cur_len = i - num_pos[num]
                left = num_pos[num] + 1
                num_pos[num] = i
            cur_max = max(cur_max, cur_len)
                

        return cur_max
