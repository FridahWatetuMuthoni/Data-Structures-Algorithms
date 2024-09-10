#reversing a string
def reverse_string(str):
    letters = []
    reversed_string = []
    
    for letter in str:
        letters.append(letter)
    
    while(len(letters) > 0):
        reversed_string.append(letters.pop())
    
    return "".join(reversed_string)
    

print(reverse_string('fridah'))
