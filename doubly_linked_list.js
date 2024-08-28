class Node {
  constructor(data, prev = null, next = null) {
    this.data = data;
    this.prev = prev;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  is_empty() {
    return this.size === 0;
  }

  insert_head(data) {
    let new_node = new Node(data);
    if (this.is_empty()) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      let current = this.head;
      new_node.next = current;
      current.prev = new_node;
      this.head = new_node;
    }
    this.size += 1;
  }

  insert_tail(data) {
    let new_node = new Node(data);
    if (this.is_empty()) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      let current = this.tail;
      current.next = new_node;
      new_node.prev = current;
      this.tail = new_node;
    }
    this.size += 1;
  }

  insert_at_index(data, index) {
    let new_node = new Node(data);
    let current = this.head;

    if (index < 0 || index > this.size) {
      console.log("out");
      return "index is out of bound";
    }
    if (index === 0) {
      this.insert_head(data);
    } else if (index === this.size) {
      this.insert_tail(data);
    } else {
      let current_index = 0;
      while (current_index < index) {
        current = current.next;
        current_index++;
      }
      let prev_node = current.prev;
      prev_node.next = new_node;
      new_node.prev = prev_node;
      new_node.next = current;
      current.prev = new_node;
    }
    this.size += 1;
  }

  get_at_index(index) {
    let current = this.head;
    let current_index = 0;

    if (index < 0 || index >= this.size) {
      return "index is out of bound";
    }

    while (current_index < index) {
      current = current.next;
      current_index++;
    }
    return current.data;
  }

  remove_at_index(index) {
    let current = this.head;
    if (index < 0 || index >= this.size) {
      return "index is out of bound";
    }
    ////if it has only one node
    if (index === 0 && this.tail === this.head) {
      this.size = 0;
      this.head = null;
      this.tail = null;
    }
    //remove at head
    else if (index === 0) {
      let current = this.head;
      let next_node = current.next;
      next_node.prev = null;
      this.head = next_node;
    }
    //remove at tail
    else if (index === this.size - 1) {
      let current = this.tail;
      let prev_node = current.prev;
      this.tail = prev_node;
    } else {
      let current_index = 0;
      while (current_index < index) {
        current = current.next;
        current_index++;
      }
      let prev_node = current.prev;
      let next_node = current.next;
      prev_node.next = next_node;
      next_node.prev = prev_node;
    }
    this.size -= 1;
  }

  clear() {
    this.head = null;
    this.size = 0;
  }
  print_list_data() {
    let current = this.head;
    let current_index = 0;
    let last_index = this.size;
    let str = "";
    while (current_index < last_index) {
      if (current_index === 0 && current.next === null) {
        str += `[Head:[d:${current.data}]]`;
      } else if (current_index === 0 && current.next !== null) {
        str += `[Head:[d:${current.data}->n:${current.next.data}]]=>`;
      } else if (current.next === null) {
        str += `[Tail:[p:${current.prev.data}->d:${current.data}]]`;
      } else if (current_index < last_index) {
        str += `[p:${current.prev.data}->d:${current.data}->n:${current.next.data}]=>`;
      }
      current_index++;
      current = current.next;
    }
    console.log(str);
  }

  print_list() {
    let current = this.head;
    let str = "";

    while (current.next !== null) {
      if (current === this.head) {
        str += `[Head=>${current.data}]=>`;
      } else {
        str += `${current.data}=>`;
      }
      current = current.next;
    }

    str += `[Tail:${current.data}]`;

    console.log(str);
  }
}

let l1 = new LinkedList();
l1.insert_head(10);
l1.insert_head(20);
l1.insert_head(30);
l1.insert_head(40);
l1.insert_head(50);
l1.insert_tail(80);
l1.insert_tail(90);
l1.insert_tail(100);
l1.insert_at_index(700, 2);
l1.insert_at_index(60, 0);
l1.insert_at_index(105, l1.size - 1);
l1.print_list();
console.log(l1.get_at_index(10));
l1.remove_at_index(4);
l1.print_list();
