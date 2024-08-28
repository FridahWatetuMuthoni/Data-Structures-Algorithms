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
  }
  //is empty
  is_empty() {
    return this.size === 0;
  }

  //insert first node
  insert_head(data) {
    let new_node = new Node(data);
    new_node.next = this.head;
    this.head = new_node;
    this.size += 1;
  }

  //insert last node
  insert_tail(data) {
    let new_node = new Node(data);
    if (this.is_empty()) {
      this.head = new_node;
    } else {
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = new_node;
    }
    this.size += 1;
  }

  //insert at index
  insert_at_index(index, data) {
    if (index > this.size) {
      this.insert_tail(data);
    } else if (index === 0) {
      this.insert_head(data);
    } else {
      let new_node = new Node(data);
      let current = this.head;
      let current_index = 0;

      while (current_index < index - 1) {
        current = current.next;
        current_index++;
      }

      let next = current.next;
      current.next = new_node;
      new_node.next = next;
      this.size += 1;
    }
  }

  //get at index
  get_at_index(index) {
    let current_index = 0;
    let current = this.head;
    if (index >= this.size || index < 0) {
      console.log("The index is out of bounds");
      return "The index is out of bounds";
    }
    while (current_index < index) {
      current = current.next;
      current_index++;
    }
    return current.data;
  }

  //remove at index
  remove_at_index(index) {
    let current = this.head;

    if (index >= this.size || index < 0) {
      return "Index is out of bound";
    }

    if (index === 0) {
      let next = this.head.next;
      this.head = next;
    } else {
      let current_index = 0;
      let prev = null;
      while (current_index < index) {
        prev = current;
        current = current.next;
        current_index++;
      }
      let next = current.next;
      prev.next = next;
    }
    this.size -= 1;
  }

  //clear list
  clear() {
    this.head = null;
    this.size = 0;
  }

  //print data
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
l1.insert_at_index(3, 700);
l1.print_list();
l1.remove_at_index(3);
l1.print_list();
//console.log(l1.get_at_index(3));
