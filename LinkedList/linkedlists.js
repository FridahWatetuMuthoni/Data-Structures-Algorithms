//time complexity => O(n)
function return_values_inter(head) {
  let current = head;
  let values = [];
  //when current.next === null it stops because it has reached the end
  while (current !== null) {
    values.push(current.data);
    current = current.next;
  }
  return values;
}

function return_values_recur(head, values = []) {
  if (head === null) {
    return values;
  }
  values.push(head.data);
  return return_values_recur(head.next, values);
}

function total_sum(head) {
  let sum = 0;
  let current = head;

  while (current !== null) {
    sum += current.data;
    current = current.next;
  }
  return sum;
}

function find_element(head, value) {
  let current = head;
  while (current !== null) {
    if (current.data === value) {
      return true;
    }
    current = current.next;
  }
  return false;
}

function get_node_value(head, index) {
  if (index < 0) {
    return "index is out of bound";
  }
  let current_index = 0;
  let current = head;
  while (current !== null) {
    if (current_index === index) {
      return current.data;
    }
    current = current.next;
    current_index++;
  }
  return null;
}

function reverse_list(head) {
  let current = head;
  let prev = null;

  while (current !== null) {
    //reverse
    let next = current.next;
    current.next = prev;

    //move forward
    prev = current;
    current = next;
  }
  // Return the new head of the reversed list
  return prev;
}

function zipper_function(head1, head2) {
  let tail = head1;
  let current_one = head1.next;
  let current_two = head2;
  let count = 1;

  while (current_one !== null && current_two != null) {
    if (count % 2 === 0) {
      tail.next = current_one;
      current_one = current_one.next;
    } else {
      tail.next = current_two;
      current_two = current_two.next;
    }

    count++;
    tail = tail.next;
  }

  //adding the remaining list at the end of the current alternated one
  if (current_one !== null) {
    tail.next = current_one;
  } else {
    tail.next = current_two;
  }

  //return the head of the new linkedlist
  return head1;
}
