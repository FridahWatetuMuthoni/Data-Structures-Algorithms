def longest_substring(str):
    seen = {}
    start = 0
    longest_string = ""
    
    for end in range(len(str)):
        letter = str[end]
        
        if letter in seen and seen[letter] >= start:
            start = seen[letter] + 1
        
        seen[letter] = end
        
        if(len(longest_string) < (end -start+1)):
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