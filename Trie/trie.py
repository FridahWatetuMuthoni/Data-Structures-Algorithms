#tries are also known as prefix trees or digital trees
#used to check if a substring is in a string
# fuctionalities: insert, search, startswith

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,str):
        current = self.root
        for letter in str:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_end_of_word = True
    
    def search(self, str):
        current = self.root
        for letter in str:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_end_of_word
    
    def starts_with(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

new_trie = Trie()
new_trie.insert('baby')
new_trie.insert('apple')
new_trie.insert('samsung')
new_trie.insert('samuel')

print(new_trie.search('anna')) #False
print(new_trie.search('samsung')) #True
print(new_trie.starts_with('sam')) #True
print(new_trie.starts_with('ann')) #False
print(new_trie.starts_with('app')) #True