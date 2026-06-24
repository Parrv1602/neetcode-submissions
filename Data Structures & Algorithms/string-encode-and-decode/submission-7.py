class Solution:

    def encode(self, strs: List[str]) -> str:
       words = ""
       '''
        Since we want to decode the strings as well, the length of the strings has to be stored, along with a character
        that separates two words, e.g.: #.
        So, store the words like this: word  length  # word2  length2  #, etc.
       '''
       for word in strs:
        words += str(len(word))
        words += "#"
        words += word

       return words


    def decode(self, s: str) -> List[str]:
        '''
        Reference: 5#Hello5#World
        String manipulation: take the length of the word just before it starts, use s[index+1: length+1]
        '''
        start_index = 0
        end_index = 0
        word_list = []

        while end_index < len(s):

            end_index = start_index #To start from the end of a new word

            while s[end_index] != "#":
                end_index += 1
            
            length = int(s[start_index:end_index]) 
            start_index = end_index + 1 #To avoid adding # to the word
            end_index = start_index + length

            word = s[start_index:end_index]
            word_list.append(word)

            start_index = end_index

        return word_list
