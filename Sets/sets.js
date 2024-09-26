const letters = new Set(["a", "b", "c", "d", "z"]);

console.log(letters);
letters.add("e");
console.log(letters);
letters.add("c");
console.log(letters);
console.log(letters.size);
console.log(letters.has("a"));
letters.delete("z");
console.log(letters.entries);

/*

1. Union => set union is when you combine set A and set B to create a new set.
union_set = A U B  
'output' => {'data', 'structure','python','Java','C'}

2. Intersection => The intersection of two sets returns a set that contains the items that are both in set A and set B.
intersection_set = A n B
'output' => {'data', 'python'}

3. Difference => The set difference returns all elements that are in set A and not in set B.
difference_set = A \ B
'output' => {'structure'}

4. Symmetric Difference => The symmetric difference returns all items that are present in set A and not B and elemets that
present in set B amd not A. 
symmetric_difference_set = A ^ B
'output' => ['structure', 'Java', 'C']

5. Issubset => Test whether a set is a subset of another
is_subset = A <= B
'output' => False

*/

const A = new Set(["data", "structure", "python"]);
const B = new Set(["python", "Java", "C", "data"]);

//union
//'output' => {'data', 'structure','python','Java','C'}
const union = new Set([...A, ...B]);
console.log(union);

//intersection
//'output' => {'data', 'python'}
const intersection = [...A].filter((value) => {
  return B.has(value);
});
console.log(intersection);

//difference
//'output' => {'structure'}
const difference = [...A].filter((value) => {
  return !B.has(value);
});
console.log(difference);

//symmetric difference
//'output' => ['structure', 'Java', 'C']
const symmetric_difference = [...A, ...B].filter((value) => {
  return !(A.has(value) && B.has(value));
});
console.log(symmetric_difference);

//issubset
//'output' => False
// Subset (Is A a subset of B?)
const is_subset = [...A].every((value) => B.has(value));
console.log(is_subset);
