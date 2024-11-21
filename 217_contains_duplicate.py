class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # method 1
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # method 2: simpler
        return len(nums)!=len(set(nums))
        
