class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        min_count = len(nums)/3
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1
        
        print(dictionary)

        result_array = []
        for num, frequency in dictionary.items():
            if frequency > min_count:
                result_array.append(num)
         
        return result_array