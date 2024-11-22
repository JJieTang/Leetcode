class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1:
        #   Time Complexity: O(n) n-str length
        #   Space Complexity: O(1) (26 chars)
        # countS = [0] * 26
        # countT = [0] * 26

        # for charS in s:
        #     countS[ord(charS) - ord('a')] += 1
        
        # for charT in t:
        #     countT[ord(charT) - ord('a')] += 1 
        
        # return countT == countS

        # method 2:
        # s_count = collections.Counter(s)
        # t_count = collections.Counter(t)
        # return s_count == t_count

        # method 3:
        #   Time Complexity: O(n*logn)
        #   Space Complexity: O(1) to O(n) depends on the way of sorting
        return sorted(s) == sorted(t)
