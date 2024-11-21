class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # method 1:
        #   Time Complexity: O(n*k*logk) n-strs len; k-each str len
        #   Space Complexity: O(nk)
        # anagrams = defaultdict(list)
        # for str in strs:
        #     sorted_str = ''.join(sorted(str))
        #     anagrams[sorted_str].append(str)
        # return list(anagrams.values())
        # method 2:
        #   Time Complexity: O(nk)
        #   Space Complexity: O(nk)
        anagrams = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char)-ord('a')] += 1
            anagrams[tuple(count)].append(str)
        return list(anagrams.values())
