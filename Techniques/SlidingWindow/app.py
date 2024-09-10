#using sliding window
def five_contigous_books_with_the_highest_price(arr,k):
    start = 0
    end = k - 1 # we are using indexes : five elements 0,1,2,3,4
    total = 0
    max = 0
    
    #calculate the total sum of the first k elements
    #we use arr[start: k] because the value at index k is not included
    for value in arr[start:k]:
        total += value
    max = total
    
    while(end < len(arr)-1):
        total = total- arr[start] + arr[end + 1]
        if(total > max):
            max = total
        start += 1
        end += 1
    return max

arr = [12,9,23,17,25,19,4,8,21,34,26,17,19,14,27,22,15,7,2,14,5,18,24]
print(five_contigous_books_with_the_highest_price(arr,5))


"""
Find the longest substring without repeatig charaters
substring => a substring is a contiguous non-empty sequence of charaters within a string.
we what the longest substring with no repeating charaters

Code:
start = 0
end = 0 
string_len = (end - start) + 1
seen = {}
loop{
    check if the letter in seen:
        if letter in seen the current string is invalid:
            del seen[letter]
            start += 1
        else:
            end += 1
}

"""

def longest_substring(str):
    seen = {}
    start = 0
    longest_string = ''
    
    for end in range(len(str)):
        current_letter = str[end]
        
        if current_letter in seen and seen[current_letter] >= start:
            # Update the start to one after the duplicate
            start = seen[current_letter] + 1
        
        # Track the index of the current letter
        seen[current_letter] = end
        
        # Check if the current window is longer than the previously recorded longest substring
        if(len(longest_string) < (end - start) + 1):
            longest_string = str[start:end+1]
            
    print(longest_string)
    return len(longest_string)

str1 = "abcabc"
longest_substring(str1)
#output = "abc" = length = 3

str2 = "bbbbb"
longest_substring(str2)
#output = "b" = length = 1

str3 = "pwwkew"
longest_substring(str3)
#output = "wke" = length = 3