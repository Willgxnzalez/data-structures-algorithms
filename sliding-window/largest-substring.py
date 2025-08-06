 # Find largest substring of consecutive unique characters within string
 
def largest_substring(string):
    if len(string) < 1: return string
    
    left = 0
    largest = ""
    window = [] # keeps track of the characters in the actual window
    for right in range(len(string)):
        while string[right] in window: # if duplicate found, move left until duplicate is removed
            window.remove(string[left])
            left += 1
        window.append(string[right]) # add first unique character whether there were duplicates before or not
        

        if right - left + 1> len(largest): # account for the newly added unique character in window by adding 1
            largest = string[left:right + 1]
        
    return largest

test1 = "larelargeststlaragele"
test2 = "abcabdcbcaa"
print("Largest Substring:", largest_substring(test1), "\n ")