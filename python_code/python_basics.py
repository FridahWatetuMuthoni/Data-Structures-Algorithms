"""
Membership Operators
These operators are used to validate the membership of an item. 
Membership means we wish to test if a given value is stored in the sequence variable, such as a string, list, or tuple. 
Two common membership operators used in Python are in and not in.
The in operator is used to check whether a value exists in a sequence. It returns True if it finds 
the given variable in the specified sequence, and False if it does not.
The 'not in' operator returns to True if it does not find a variable in the specified sequence and 
False if it is found.
"""

mylist1 = [100, 20,30,40]
mylist2  = [10,50,60,90]

if mylist1[1] in mylist2:
    print("elements are overlapping")
else:
    print('elements are not overlapping')
    
mylist = [100, 210, 430, 840, 108]
val = 104
if val not in mylist:
    print('Value is not present in mylist')
else:
    print('Value is present in my list')


"""
Identity operators
Identity operators are used to compare objects. The different types of identity operators are is 
and is not, which are defined as follows.
The is operator is used to check whether two variables refer to the same object. This is different 
from the equality (==) operator. In the equality operator, we check whether two variables are 
equal. It returns True if both side variables point to the same object; if not, then it returns False:
The is not operator is used to check whether two variables point to the same object or not. True
is returned if both side variables point to different objects, otherwise, it returns False:
"""

first_list = []
second_list = []

if first_list == second_list:
    print('Both are equal')
else:
    print('Both are not equal')

if first_list is second_list:
    print('Both variables are pointng to the same object')
else:
    print('Both objects are not pointing to the same object')

third_list = first_list

if first_list is third_list:
    print('Both variables are pointng to the same object')
else:
    print('Both objects are not pointing to the same object')
    
if first_list is not second_list:
    print('Both variables are pointng to the same object')
else:
    print('Both objects are not pointing to the same object')


# Dictornary Data struture

person  = {}
person['name'] = 'Fridah'
person['lastname'] = 'Watetu'
person['age'] = 31
person['address'] = 'Nairobi'
person['married'] = False
person['religous'] = False

print(person)
print(person['name'])
print( 'name' in person)
print('fname' not in person)
print(len(person))
print(person.get('age'))
print(person.items())
print(person.keys())
print(person.values())
print(person.pop('married'))
print(person.popitem()) #removes the last key-value pair added in the dictornary

person_two = {
    'children':False,
    'country':'Kenya',
    'citizen':True,
    'age':30
}

"""
Merging one dictornary with another. Firstly it checks whether a key of the second
dictornary is present on the first dictornary, the corresponding value is them updated.
if the key is not present in the first dictornary, then the key-value pair is added
"""

person.update(person_two)
print(person)

