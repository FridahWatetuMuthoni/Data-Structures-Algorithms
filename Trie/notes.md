# Trie Data structure

## Introduction

A Trie (pronounced "try") is a type of tree data structure used primarily for storing and searching strings, typically words in a dictionary. It's also known as a prefix tree because it efficiently handles scenarios where you need to search for keys with a common prefix.

### Key Concepts:

1. Nodes and Edges:
   Each node in a Trie represents a single character of a string.
   The edges between nodes represent the transition from one character to the next in the string.

2. Root Node:
   The Trie starts with an empty root node, which doesn't contain any character.

3. Insertion:
   Words are inserted into the Trie character by character. For each character in the word, if there isn't a corresponding child node, a new node is created.

4. Search:
   To search for a word, you follow the sequence of characters from the root node down through the nodes, checking if each character exists in the Trie. If you reach the end of the word in the Trie, the word is present.

5. End of Word Markers:
   Nodes can have a boolean flag to indicate the end of a word. This helps in differentiating between prefixes and full words.

Example:
Consider the insertion of the words "bat", "ball", and "batman":

Insert "bat":

      Root
       |
       b
       |
       a
       |
       t (End of word)

Insert "ball":

      Root
       |
       b
       |
       a
       |
       t (End of word) -- l -- l (End of word)

Insert "batman":

      Root
       |
       b
       |
       a
       |
       t (End of word) -- m -- a -- n (End of word)
       |
       l -- l (End of word)

## Operations:

Insert: Adds a word to the Trie.
Search: Checks if a word is in the Trie.
Starts With: Checks if there's any word in the Trie that starts with a given prefix.
Deletion: This is more complex as it involves removing nodes only if they are not part of another word.

## Applications:

1. Autocomplete: Predicting the next word or suggesting words as the user types.
2. Spell Checkers: Quickly searching for words in a dictionary.
3. IP Routing: In networking, Tries are used for longest prefix matching.
4. DNA Sequence Analysis: Tries can help in storing and searching DNA sequences.
