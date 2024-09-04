class MinHeap {
  constructor() {
    this.heap = [];
    this.size = 0;
  }

  is_empty() {
    return this.size === 0;
  }

  insert(data) {
    this.heap.push(data);
    this.size += 1;
    this.bubble_up(this.size - 1);
  }

  remove() {
    if (this.is_empty()) {
      throw new Error("Heap is empty");
    }

    let root_value = this.heap[0];
    this.heap[0] = this.heap[this.size - 1];
    this.heap.pop();
    this.size -= 1;
    if (!this.is_empty()) {
      this.bubble_down(0);
    }
    return root_value;
  }

  bubble_up(index) {
    while (index > 0) {
      let parent_index = this.parent_index(index);

      if (this.heap[index] < this.heap[parent_index]) {
        [this.heap[index], this.heap[parent_index]] = [
          this.heap[parent_index],
          this.heap[index],
        ];
        index = parent_index;
      } else {
        break;
      }
    }
  }

  bubble_down(index) {
    while (true) {
      let left_index = this.get_left_index(index);
      let right_index = this.get_right_index(index);
      let smallest = index;

      if (
        left_index < this.size &&
        this.heap[left_index] < this.heap[smallest]
      ) {
        smallest = left_index;
      }
      if (
        right_index < this.size &&
        this.heap[right_index] < this.heap[smallest]
      ) {
        smallest = right_index;
      }

      if (smallest == index) {
        break;
      }

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }

  get_parent_index(index) {
    let parent = Math.floor((index - 1) / 2);
    return parent;
  }

  get_left_index(index) {
    let left = index * 2 + 1;
    return left;
  }

  get_right_index(index) {
    let right = index * 2 + 2;
    return right;
  }

  heapfy(arr) {
    this.size = arr.length;
    for (let i = 0; i < this.size; i++) {
      this.insert(arr[i]);
    }
    return this.heap;
  }

  heapify(arr) {
    this.heap = arr;
    this.size = arr.length;

    for (let i = Math.floor(this.size / 2) - 1; i >= 0; i--) {
      this.bubble_down(i);
    }
    return this.heap;
  }

  heap_sort() {
    let arr = [...this.heap];
    let sorted_values = [];
    let size = this.size;

    while (arr.length > 0) {
      let value = arr[0];
      arr[0] = arr[this.size - 1];
      arr.pop();
      size -= 1;
      this.bubble_down(0);
      sorted_values.push(value);
    }

    return sorted_values;
  }

  heap_sort_edited() {
    let copy_heap = [...this.heap];
    let sorted_values = [];

    while (!this.is_empty()) {
      sorted_values.push(this.remove());
    }

    // Restore the original heap structure
    this.heap = copy_heap;
    this.size = copy_heap.length;

    return sorted_values;
  }
}
