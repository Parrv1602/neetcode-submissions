class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Use a default dict as you can store multiple values for a given key
        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            #By default, a default dictionary creates an empty list
            #So if the sorted word isn't there, the word (value) will still be appended
            #with 
            anagram_dict[sorted_word].append(word)
        
        return list(anagram_dict.values())

            
        '''
        #Store sorted versions of strings in strs
        sorted_strs_frequency = {}
        sorted_strs_translation = {}
        return_list = []
        temp_list = []
        for word in strs:

            sorted_word = "".join(sorted(word))

            if sorted_word not in sorted_strs_frequency.keys():

                sorted_strs_frequency[sorted_word] = 1
                sorted_strs_translation[word] = sorted_word

            else:
                sorted_strs_frequency[sorted_word] += 1
                sorted_strs_translation[word] = sorted_word
                temp_list.append(word)


        
        print(sorted_strs_frequency)
        print(sorted_strs_translation)
        '''
                

    

        
