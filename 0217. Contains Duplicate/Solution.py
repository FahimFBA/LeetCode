class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set() # Create a hashset
        # Going through every value in the input array nums
        for i in nums: 
            if i in hashset:
                return True
            hashset.add(i)
        return False
        