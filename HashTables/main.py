#INBUILT HASHMAPS

# Dictionary : all keys need to be initialized
city_map = {}
cities = ['Calgary', 'Vancouver','Toronto']
city_map['canada'] = []
city_map['canada'] += cities
print(city_map)

#DefaultDict: all keys are already initialized
from collections import defaultdict

city_map_2 = defaultdict(list)

cities_2 = ['Calgary', 'Vancouver','Toronto']
city_map_2['canada'] += cities
print(city_map_2)
print(city_map_2.keys()) #keys
print(city_map_2.values()) #values
print(city_map_2.items()) #key,value pairs


#CREATED HASHMAPS

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for i in range(self.size)]
    
    def hash(self,key):
        total = 0
        for char in key:
            total += ord(char)
        index = total % self.size
        return index
    
    def get(self,key):
        index = self.hash(key)
        elements = self.hashtable[index]
        
        for element in elements:
            if(element[0]== key):
                return element[1]
    
    def delete(self,key):
        index = self.hash(key)
        self.hashtable[index] = None
    
    def add(self,key,value):
        index = self.hash(key)
        found = False
        for i, element in enumerate(self.hashtable[index]):
            if len(element) == 2 and element[0]==key:
                self.hashtable[index][i] = (key, value)
                found = True
                break
        if not found:
            self.hashtable[index].append((key,value))
    
    def __getitem__(self,key):
        index = self.hash(key)
        arr =  self.hashtable[index]
        for item in arr:
            if item[0] == key:
                return item[1]
    
    def __setitem__(self,key,value):
        index = self.hash(key)
        found = False
        
        for i, element in enumerate(self.hashtable[index]):
            if(len(element) == 2 and element[0] == key):
                found = True
                self.hashtable[index][i] = (key,value)
                break
        if not found:
            self.hashtable[index].append((key,value))
        
    def __delitem__(self,key):
        index = self.hash(key)
        for i, element in enumerate(self.hashtable[index]):
            if element[0] == key:
                del self.hashtable[index][i]

hashMap = HashTable(10)
hashMap.add('march 6',3000)
hashMap['march 8'] = 6000
hashMap['march 9'] = 7000
hashMap['march 17'] = 9000
print(hashMap['march 17'])
print(hashMap['march 6'])
print(hashMap['march 9'])
del hashMap['march 8']
print(hashMap.hashtable)
