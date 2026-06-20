class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Output an array that contains elements that occur greater than or equal to k number of times.
        For example, if 2 and 3 occur two or more times, then append them to the return array
        '''

        dictionary = defaultdict(int)
        for num in nums:
            #Default dictionary initalises keys' values to 0
            dictionary[num] += 1

        array = []
        for number, frequency in dictionary.items():
            array.append([frequency, number])
        
        #.sort() sorts an array (if it contains arrays as elements) based on the first element in the array
        #So, since frequency is placed first, it sorts the number and its frequency by its frequency in ascending order
        #Also .sort() sorts the array in-place.
        array.sort()

        return_array = []
        while k > len(return_array):
            #Return the number rather than the frequency. Element is array of two elements, 2nd element contains num
            most_frequent_element = array.pop()
            return_array.append(most_frequent_element[1])
        return return_array


