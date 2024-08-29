class List {
  constructor() {
    this.items = [];
    this.pos = 0; // Current position in the list
  }

  // Returns the number of elements in the list
  length() {
    return this.items.length;
  }

  // Clears all elements from the list
  clear() {
    this.items = [];
    this.pos = 0;
  }

  // Returns string representation of the list
  toString() {
    return this.items.join(", ");
  }

  // Returns element at current position
  getElement() {
    if (this.pos >= 0 && this.pos < this.items.length) {
      return this.items[this.pos];
    } else {
      console.log("Current position is out of bounds");
      return undefined;
    }
  }

  // Inserts new element after the current position
  insert(element) {
    if (this.pos >= 0 && this.pos < this.items.length) {
      this.items.splice(this.pos + 1, 0, element);
    } else {
      console.log("Cannot insert, position is out of bounds");
    }
  }

  // Adds new element to the end of the list
  append(element) {
    this.items.push(element);
  }

  // Removes element from the list
  remove(element) {
    const index = this.items.indexOf(element);
    if (index !== -1) {
      this.items.splice(index, 1);
      if (this.pos >= this.items.length) {
        this.pos = this.items.length - 1; // Adjust position if needed
      }
    } else {
      console.log("Element not found in the list");
    }
  }

  // Sets current position to the first element
  front() {
    this.pos = 0;
  }

  // Sets current position to the last element
  end() {
    this.pos = this.items.length - 1;
  }

  // Moves current position back one element
  prev() {
    if (this.pos > 0) {
      this.pos--;
    } else {
      console.log("Already at the beginning of the list");
    }
  }

  // Moves current position forward one element
  next() {
    if (this.pos < this.items.length - 1) {
      this.pos++;
    } else {
      console.log("Already at the end of the list");
    }
  }

  // Returns the current position in the list
  currPos() {
    return this.pos;
  }

  // Moves the current position to a specified position
  moveTo(position) {
    if (position >= 0 && position < this.items.length) {
      this.pos = position;
    } else {
      console.log("Position out of bounds");
    }
  }
}

// Example usage
const myList = new List();
myList.append("Apple");
myList.append("Banana");
myList.append("Cherry");

console.log("List:", myList.toString()); // List: Apple, Banana, Cherry

myList.front();
console.log("Current Position (front):", myList.currPos()); // 0

myList.next();
console.log("Current Position (next):", myList.currPos()); // 1

myList.insert("Blueberry");
console.log("List after inserting Blueberry:", myList.toString()); // Apple, Blueberry, Banana, Cherry

myList.remove("Banana");
console.log("List after removing Banana:", myList.toString()); // Apple, Blueberry, Cherry

console.log("Element at current position:", myList.getElement()); // Cherry

myList.moveTo(0);
console.log("Element at position 0:", myList.getElement()); // Apple

myList.clear();
console.log("List after clear:", myList.toString()); // (empty)
