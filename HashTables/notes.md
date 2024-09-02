# HashMaps and HashTables

## Introduction

Hashmap is a datastructure that stores information called values and it pairs it with unique identifiers called keys.
Example a Capital City Database
We can use the country as the key and the capital city as the value.

## Benefits of HashMaps

1. Custom keys are easier for software wngineers to work with.
2. Hashmaps allow for search in 0(1) whereas arrays/linkedlits are O(n).

## How hashmaps work

Hashmaps are commonly built of a predefined data structure like an array.Like hashmaps, arrays do also have keys that store values, for arrays though, the key is a preset number called an index, which starts at zero. A hashmap is created from an array thru the use of a hash function, which takes in a custom data that we want to assign to a key like a country and maps this data to an index on the array. These hash functions can get complex, especially as they have to tackle issues that comeup when mapping data to indices. The most common issue that comes up is called a collision, and it occurs when a hash function tries to assign a piece of data to an already used index. In this case the hash function should have an effiecient way to re-assign the data to a different , non used index.
Key must be an immutable data type.
