class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(zip(nums, range(len(nums))))
        firstNum = 0
        secondNum = len(nums) - 1
        while firstNum < secondNum:
            if sortedNums[firstNum][0] + sortedNums[secondNum][0] == target:
                return [sortedNums[firstNum][1], sortedNums[secondNum][1]]
            elif sortedNums[firstNum][0] + sortedNums[secondNum][0] < target:
                firstNum += 1
            elif sortedNums[firstNum][0] + sortedNums[secondNum][0] > target:
                secondNum -= 1