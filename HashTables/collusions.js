class HashTable {
  constructor(size) {
    this.size = size;
    this.hashtable = Array.from({ length: this.size }, () => []);
  }

  hash(key) {
    let total = 0;
    for (let i = 0; i < key.length; i++) {
      total += key.charCodeAt(i);
    }
    let index = total % this.size;
    return index;
  }

  get(key) {
    let index = this.hash(key);
    for (let i = 0; i < this.hashtable[index].length; i++) {
      if (this.hashtable[index][i][0] === key) {
        return this.hashtable[index][i][1];
      }
    }
  }

  set(key, value) {
    let index = this.hash(key);
    let arr = this.hashtable[index];
    let found = false;

    for (let i = 0; i < arr.length; i++) {
      if (arr[i][0] === key) {
        arr[i] = [key, value];
        found = true;
        break;
      }
    }

    if (!found) {
      arr.push([key, value]);
    }
  }

  delete(key) {
    let index = this.hash(key);
    let arr = this.hashtable[index];

    for (let i = 0; i < arr.length; i++) {
      if (arr[i][0] === key) {
        arr.splice(i, 1);
      }
    }
  }
}

// Example usage
const hashMap = new HashTable(10);
hashMap.set("march 6", 3000);
hashMap.set("march 8", 6000);
hashMap.set("march 9", 7000);
hashMap.set("march 17", 9000);
console.log(hashMap.get("march 17")); // Output: 9000
console.log(hashMap.get("march 6")); // Output: 3000
console.log(hashMap.get("march 9")); // Output: 7000
hashMap.delete("march 8");
console.log(hashMap.hashtable); // Output: hash table content
