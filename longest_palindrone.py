# Find the longest palindrone in a given string

class Solution:
    def longestPalindrome(self, str1: str) -> str:
        str1_reversed = str1[::-1]
        print(str1_reversed)
        
        # If string is 1 length then it cannot  have any palins
        len_str1 = len(str1)
        if len_str1 <=1:
            return ""
        
        # Start with max length going smaller uptil 2
        palin_size = range(len_str1, 2, -1)
        #no_of_substr = range(1, len_str1-1)
        min_palin_size = 2 #should be at least 2 chars
        
        # Initialize defaults
        max_size = 0
        palin_location = 0
        palin_found = False
        
        for current_size in palin_size:
            # Whenever you find a common string - immediately check for start indices
            all_locations = range(len_str1 - current_size + 1)
            
            
            for i in all_locations:
                if str1[i:i+current_size] in str1_reversed:
                    if str1_reversed[len_str1 - i - current_size: len_str1 - i] == str1[i:i+current_size]:
                        palin_location = i
                        max_size = current_size
                        palin_found = True
                        
            if (palin_found == True):
                break
        
        if (palin_found == True):
            print("palin = ")
            print(str1[palin_location:palin_location + max_size])
        else:
            print("Nothing found")
    

sol = Solution()
sol.longestPalindrome("amadam")
