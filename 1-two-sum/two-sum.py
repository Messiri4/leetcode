class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Store previously seen numbers as keys and their indices as values.
        hashset = {}

        # Loop through each number and its index.
        for index, num in enumerate(nums):
            # Calculate the number needed to reach the target.
            diff = target - num

            # Check whether that matching number has already been stored.
            if diff in hashset:
                # Return the matching number's index and the current index.
                return [hashset[diff], index]

            # Save the current number and its index for later iterations.
            hashset.update({num: index})