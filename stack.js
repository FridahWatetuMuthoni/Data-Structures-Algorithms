class Stack {
  constructor() {
    this.datastore = [];
  }

  size() {
    return this.datastore.length;
  }

  is_empty() {
    return this.datastore.length === 0;
  }

  clear() {
    this.datastore = [];
  }

  peek() {
    if (this.is_empty()) {
      console.log("stack is empty");
      return undefined;
    } else {
      return this.datastore[this.datastore.length - 1];
    }
  }

  push(data) {
    this.datastore.push(data);
  }

  pop() {
    if (this.is_empty()) {
      console.log("The stack is empty");
      return undefined;
    }

    return this.datastore.pop();
  }
}

const myStack = new Stack();
myStack.push("Apple");
myStack.push("Banana");
myStack.push("Cherry");

console.log("Top item:", myStack.peek()); // Cherry
console.log("Stack size:", myStack.size()); // 3

console.log("Popped item:", myStack.pop()); // Cherry
console.log("Top item after pop:", myStack.peek()); // Banana
console.log("Stack size after pop:", myStack.size()); // 2

myStack.clear();
console.log("Stack size after clear:", myStack.size()); // 0
console.log("Top item after clear:", myStack.peek()); // Stack is empty
