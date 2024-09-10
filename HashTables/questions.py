"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An anagram is a word ot pharse formed by rearranging the letters of a different word or pharse, typically using all the original letter exactly once.
Example:
input  = ['eat','tea','tan','ate','nat','bat']
output = [['bat'],['nat','tan'],['ate','eat','tea']]
"""
from collections import defaultdict
class Anagrams:
    def group_anagrams(self, arr):
        anagram_map = defaultdict(list)
        result = []
        for value in arr:
            sorted_word = tuple(sorted(value))
            anagram_map[sorted_word].append(value)
        
        for value in anagram_map.values():
            result.append(value)
        
        return result

anagram = Anagrams()
input = ['eat','tea','tan','ate','nat','bat']
print(anagram.group_anagrams(input))



#O(n)
def two_sum_unsorted(arr, target):
    seen = {}
    
    for i, value in enumerate(arr):
        compliment = target - value
        if(compliment in seen):
            return [compliment, value]
        else:
            print(seen)
            seen[value] = i
    return None

arry = [3, 5, 2, -4, 8, 11]
total = 19
print(two_sum_unsorted(arry,total))



"""
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

"""

import csv
from pathlib import Path

class HashMap:
    def __init__(self,size):
        self.size = size
        self.hashtable = [[] for i in range(self.size)]
        self.max = 0
        self.days = 0
        self.total = 0
        
    def create_hashtable(self):
        file_path = Path("./HashTables/weather.csv").resolve()
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if(row[0] == 'date'):
                    continue
                else:
                    self.add(row[0],row[1])
                    if(self.max < int(row[1])):
                        self.max = int(row[1])
                    self.days += 1
                    self.total += int(row[1])
    
    def hash(self,key):
        total = 0
        for letter in key:
            total += ord(letter)
        return total % self.size
    
    def average_temp(self):
        return self.total / self.days
    
    def add(self,key,value):
        index = self.hash(key)
        arr = self.hashtable[index]
        found = False

        for element in arr:
           if(len(element) == 2 and element[0] == key):
               element = [key, value]
               found = True
               break
        if not found:
            arr.append([key,value])

    
    def get(self,key):
        index = self.hash(key)
        arr = self.hashtable[index]
        
        for element in arr:
            if element[0] == key:
                return element[1]
    
    def delete(self,key):
        index = self.hash(key)
        arr = self.hashtable[index]
        
        for i,element in enumerate(arr):
            if element[0] == key:
                del self.hashtable[index][i]

if __name__ == '__main__':
    hashmap = HashMap(20)
    hashmap.create_hashtable()
    print(hashmap.hashtable)
    print(hashmap.get('Jan 9'))
    print(hashmap.delete('Jan 10'))
    print(hashmap.hashtable)
    print(hashmap.max)
    print(hashmap.average_temp())
    print(hashmap.days)
