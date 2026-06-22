class Solution:
    def __init__(self):
        self.length = []

    def encode(self, strs: List[str]) -> str:
        '''
        return_string = ""

        for word in strs:
            #Create a pattern in the string: length of string followed by string followed by string and then a separator
            return_string += str(len(word))
            return_string += word
            return_string += "#"
            
        '''
        return_array = ""
        for word in strs:
            return_array += str(len(word))
            return_array += "#"
            return_array += word

        return return_array


    def decode(self, s: str) -> List[str]:
        #E.g.: 5#Hello5#World

        return_list = []
        start_index = 0
        end_index = 0
        
        while start_index < len(s):
            #Increment end_index until it reaches end of word indicated by a #
            end_index = start_index
            while s[end_index] != "#":
                end_index += 1
            
            #Obtain length of the word which is stored in the string
            #The length of the word is stored before the hashtag
            word_length = int(s[start_index:end_index])
            #Now want to extract the word
            start_index = end_index + 1
            end_index = start_index + word_length
            return_list.append(s[start_index:end_index])

            #Now that the word is appended, move onto the next word
            start_index = end_index
        
        return return_list


            
            


