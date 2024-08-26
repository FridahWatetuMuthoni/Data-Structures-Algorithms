class Queue {
  constructor() {
    this.datastore = [];
  }

  is_empty() {
    return this.datastore.length === 0;
  }

  size() {
    return this.datastore.length;
  }

  clear() {
    this.datastore = [];
  }

  peek() {
    if (this.is_empty()) {
      console.log("the queue is empty");
      return undefined;
    } else {
      return this.datastore[0];
    }
  }

  enqueue(data) {
    this.datastore.push(data);
  }

  dequeue() {
    if (this.is_empty()) {
      console.log("the queue is empty");
    } else {
      return this.datastore.shift();
    }
  }
}

// Example usage
const myQueue = new Queue();
myQueue.enqueue("Apple");
myQueue.enqueue("Banana");
myQueue.enqueue("Cherry");

console.log("Front item:", myQueue.peek()); // Apple
console.log("Queue size:", myQueue.size()); // 3

console.log("Dequeued item:", myQueue.dequeue()); // Apple
console.log("Front item after dequeue:", myQueue.peek()); // Banana
console.log("Queue size after dequeue:", myQueue.size()); // 2

myQueue.clear();
console.log("Queue size after clear:", myQueue.size()); // 0
console.log("Front item after clear:", myQueue.peek()); // Queue is empty
