class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Can use binary search to only search part of array that is lesser than the target.
        '''
        left_pointer, right_pointer = 0, len(numbers)-1

        numbers.sort()
        while right_pointer > left_pointer:
                if numbers[left_pointer] + numbers[right_pointer] > target: #Value at end too large
                    right_pointer -= 1
                elif numbers[left_pointer] + numbers[right_pointer] < target: #Value at the beginning too small
                    left_pointer += 1
                else:
                    return [left_pointer+1, right_pointer+1]

            