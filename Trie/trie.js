// search, startswith, insert

class TrieNode {
  constructor() {
    this.children = {};
    this.is_end_of_word = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(str) {
    let current = this.root;

    for (let letter of str) {
      if (!(letter in current.children)) {
        current.children[letter] = new TrieNode();
      }
      current = current.children[letter];
    }

    current.is_end_of_word = true;
  }

  search(str) {
    let current = this.root;

    for (let letter of str) {
      if (!(letter in current.children)) {
        return false;
      }
      current = current.children[letter];
    }

    return current.is_end_of_word;
  }

  starts_with(prefix) {
    let current = this.root;

    for (let letter of prefix) {
      if (!(letter in current.children)) {
        return false;
      }
      current = current.children[letter];
    }
    return true;
  }
}

let new_trie = new Trie();
new_trie.insert("baby");
new_trie.insert("apple");
new_trie.insert("samsung");
new_trie.insert("samuel");

console.log(new_trie.search("anna")); //False
console.log(new_trie.search("samsung")); //True
console.log(new_trie.starts_with("sam")); //True
console.log(new_trie.starts_with("ann")); //False
console.log(new_trie.starts_with("app")); //True
