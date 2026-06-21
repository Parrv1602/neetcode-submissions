class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Find the k number of most frequent elements in an array
        '''
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] += 1
        
        array = []
        for num, frequency in dictionary.items():
            array.append([frequency, num])
        
        array.sort()
        #The most frequent numbers will be last
        K = 0
        most_frequent_elements = []
        while k > K:
            #pop the last element which is the number with the largest frequency
            most_frequent_elements.append(array.pop()[1])
            K += 1

        return most_frequent_elements


