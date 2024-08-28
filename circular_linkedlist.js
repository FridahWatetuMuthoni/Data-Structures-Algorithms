class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
    this.tail = null;
  }

  is_empty() {
    return this.size === 0;
  }

  insert_head(data) {
    let new_node = new Node(data);
    if (this.is_empty()) {
      this.head = new_node;
      new_node.next = this.head;
      this.tail = new_node;
    } else {
      let current = this.head;
      new_node.next = current;
      this.head = new_node;
      this.tail.next = this.head;
    }

    this.size += 1;
  }

  insert_tail(data) {
    let new_node = new Node(data);
    if (this.is_empty()) {
      this.head = new_node;
      this.tail = new_node;
      new_node.next = this.head;
    } else {
      this.tail.next = new_node;
      this.tail = new_node;
      this.tail.next = this.head;
    }
    this.size += 1;
  }

  insert_at_index(data, index) {
    if (index < 0 || index >= this.size) {
      return "Index is out of bound";
    }

    if (index === 0) {
      this.insert_head(data);
    }
    if (index === this.size) {
      this.insert_tail(data);
    }

    let new_node = new Node(data);
    let current = this.head;
    let prev = null;
    let current_index = 0;
    while (current_index < index) {
      prev = current;
      current = current.next;
      current_index++;
    }
    prev.next = new_node;
    new_node.next = current;

    this.size += 1;
  }

  get_at_index(index) {
    if (index < 0 || index >= this.size) {
      return "Index is out of bound";
    }
    let current = this.head;
    let current_index = 0;
    while (current_index < index) {
      current = current.next;
      current_index++;
    }
    return current.data;
  }

  remove_at_index(index) {
    if (index < 0 || index >= this.size) {
      return "Index is out of bound";
    }
    let current = this.head;
    let current_index = 0;
    let prev = null;

    if (index === 0) {
      let current = this.head;
      let next_node = current.next;
      this.head = next_node;
      this.tail.next = this.head;
    } else {
      while (current_index < index) {
        prev = current;
        current = current.next;
        current_index++;
      }
      let next_node = current.next;
      prev.next = next_node;
      if (current === this.tail) {
        this.tail = prev;
      }
    }
    this.size -= 1;
  }

  clear() {
    this.head = null;
    this.size = 0;
    this.tail = null;
  }

  print_list() {
    if (this.is_empty()) {
      console.log("The list is empty");
      return;
    }

    let current = this.head;
    let str = "";

    do {
      if (current === this.head) {
        str += `[Head=>${current.data}]=>`;
      } else {
        str += `${current.data}=>`;
      }
      current = current.next;
    } while (current !== this.head);

    str += `[Tail:${this.tail.data}]`;

    console.log(str);
  }
}

let l1 = new LinkedList();
l1.insert_head(10);
l1.insert_head(20);
l1.insert_head(30);
l1.insert_head(40);
l1.insert_tail(80);
l1.insert_tail(90);
l1.insert_tail(100);
l1.print_list();
l1.insert_at_index(3, 700);
l1.print_list();
l1.remove_at_index(3);
l1.print_list();
//console.log(l1.get_at_index(3));
