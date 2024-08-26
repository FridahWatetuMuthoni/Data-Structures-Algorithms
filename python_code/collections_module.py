"""
Python's collections module:
The collections module provides different types of containers, which are objects that are used 
to store different objects and provide a way to access them. Before accessing these, let’s consider 
briefly the role and relationships between modules, packages, and scripts.
A module is a Python script with the .py extension that contains a collection of functions, classes, 
and variables. A package is a directory that contains collections of modules; it has an __init__.
py file, which lets the interpreter know that it is a package. A module can be called into a Python 
script, which can in turn make use of the module’s functions and variables in its code. In Python, 
we can import these to a script using the import statement. Whenever the interpreter encounters 
the import statement, it imports the code of the specified module.
Python Collection Module:
1. namedtuple => Creates a tuple with named fields similar to regular tuples.
2. deque => Doubly-linked lists that provide efficient adding and removing of items 
from both ends of the list.
3. defaultdict => A dictionary subclass that returns default values for missing keys.
4. ChainMap => A dictionary that merges multiple dictionaries.
5. Counter => A dictionary that returns the counts corresponding to their objects/key.
6. UserDict, UserList, UserString => These data types are used to add more functionalities to their base data 
structure, such as a dictionary, list, and string. And we can create 
subclasses from them for custom dict/list/string.
"""

from collections import namedtuple, deque, OrderedDict,defaultdict, ChainMap, Counter, UserDict, UserList, UserString

#Named tuples

Book = namedtuple ('Book', ['name', 'ISBN', 'quantity'])
Book1 = Book('Hands on Data Structures', '9781788995573', '50')
print('Using index ISBN:' + Book1[1])
print('Using key ISBN:' + Book1.ISBN)

#Deque
s = deque() # Creates an empty deque
print(s)
my_queue = deque([1, 2, 'Name'])
my_queue.append('age') #Insert 'age' at the right end of the list.
my_queue.appendleft('age') #Insert 'age' at the left end of the list.
my_queue.pop() #Delete the rightmost value.
my_queue.popleft() #Delete the leftmost value.

print(my_queue)

#Ordered dictionaries
#An ordered dictionary is a dictionary that preserves the order of the keys that are inserted. 
# If the key order is important for any application, then OrderedDict can be used:
od = OrderedDict({'my': 2, 'name ': 4, 'is': 2, 'Mohan' :5})
od['hello'] = 4
print(od)


#Default dictionary
#The default dictionary (defaultdict) is a subclass of the built-in dictionary class (dict) that 
#has the same methods and operations as that of the dictionary class, with the only difference 
#being that it never raises a KeyError, as a normal dictionary would. defaultdict is a convenient 
#way to initialize dictionaries:
dd = defaultdict(int)
words = str.split('data python data data structure data python')
for word in words:
    dd[word] += 1
print(dd)

#ChainMap object
#ChainMap is used to create a list of dictionaries. The collections.ChainMap data structure 
#combines several dictionaries into a single mapping. Whenever a key is searched in the chainmap, 
#it looks through all the dictionaries one by one, until the key is not found:
dict1 = {"data": 1, "structure": 2}
dict2 = {"python": 3, "language": 4}
chain = ChainMap(dict1, dict2)
print(chain)
print(list(chain.keys()))
print(list(chain.values()))
print(chain["data"])
print(chain["language"])

#Counter objects
#As we discussed earlier, a hashable object is one whose hash value will remain the same during 
#its lifetime in the program. counter is used to count the number of hashable objects. Here, the 
#dictionary key is a hashable object, while the corresponding value is the count of that object. In 
#other words, counter objects create a hash table in which the elements and their count are stored as dictionary keys and value pairs.
inventory = Counter('hello')
print(inventory)
print(inventory['l'])
print(inventory['e'])
print(inventory['o'])

#UserDict
#Python supports a container, UserDict, present in the collections module, that wraps the dictionary 
#objects. We can add customized functions to the dictionary. This is very useful for applications 
#where we want to add/update/modify the functionalities of the dictionary. Consider the example 
#code below where pushing/adding a new data element is not allowed in the dictionary:
class MyDict(UserDict):
    def push(self, key, value):
        raise RuntimeError('cannot insert')
d = MyDict({'ab':1, 'bc':2, 'cd':3})
d.push('b',2)

#UserList
#A UserList is a container that wraps list objects. It can be used to extend the functionality of the 
#list data structure. Consider the example code below, where pushing/adding a new data element 
#is not allowed in the list data structure:
class MyList(UserList):
    def push(self, key):
        raise RuntimeError("Cannot insert in the list")
d = MyList([11, 12, 13])
d.push(2)


#UserString
#Strings can be considered as an array of characters. In Python, a character is a string of one length 
#and acts as a container that wraps a string object. It can be used to create strings with customized 
#functionalities. An example could look like the following:
class MyString(UserString):
    def append(self, value):
        self.data += value
s1 = MyString("data")
print("Original:", s1)
s1.append('h')
print("After append: ", s1)

