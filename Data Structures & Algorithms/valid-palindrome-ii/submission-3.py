class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1
        
        #Creating a helper function
        #This function  will determine if the remaining characters (after "deleting" the character), result in a palindrome
        def palindrome_helper(left_pointer, right_pointer):
            while left_pointer < right_pointer:
                if s[left_pointer] != s[right_pointer]:
                    return False
                
                left_pointer += 1
                right_pointer -= 1
            
            return True
        
        while left_pointer < right_pointer:
            #Found two characters not equal to each other, perform "deletion".
            if s[left_pointer] != s[right_pointer]:
                #Check if either deletion of left element or right element and elements forward or before it result in a palindrome
                #if it does, then string is palindrome, if it doesn't string is not a palindrome or more chars need to be deleted
                return (palindrome_helper(left_pointer+1, right_pointer)) or palindrome_helper(left_pointer, right_pointer-1)
            
            left_pointer += 1
            right_pointer -= 1
        
        return True
 