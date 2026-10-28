class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {} #create a hashmap

        for i, n in enumerate(nums): #loop through the index and value
            diff = target - n  #target = diff + n
                                # where diff is value to be found
                                # and n represents each value in the list
            
            if diff in hashMap: # if diff already in the hashmap
                return [hashMap[diff], i] # return the value of diff found earlier
                                        # and current index 'i' (which is also the index of n)
            hashMap[n] = i # store the current value (n) and its index

        