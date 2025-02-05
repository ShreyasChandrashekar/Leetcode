class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}
      
        for i in range(len(nums)):
            countMap[nums[i]] = 1 + countMap.get(nums[i], 0) # creates the Hash Map with the numbers and their Frequencies
                                                             # {1: 3, 2: 2, 3: 1}
        
        arr = [[] for i in range(len(nums) + 1)] # creates the array with size of the input array
    
        for num, count in countMap.items():
            arr[count].append(num)

        # Appending to the new array using the count(frequencies) of the numbers as index
        # And then appending the number to that index
        #   0   1    2    3    4   5   6
        # [[], [3], [2], [1], [], [], []]

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res 

# Time Complexity Analysis

# Time Complexity : O(n) Because you will make atleast one pass on the array
# Space Complexity : O(n) Space required for the HashMap / Dictionary