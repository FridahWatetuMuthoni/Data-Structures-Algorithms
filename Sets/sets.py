"""
SETS:
A set is an unordered collection of hashable objects. It is iterable, mutable, and has unique elements. 
The order of the elements is also not defined. While the addition and removal of items are allowed, 
the items themselves within the set must be immutable and hashable. Sets support membership 
testing operators (in, not in), and operations such as intersection, union, difference, and 
symmetric difference. Sets cannot contain duplicate items. They are created by using the built-in 
set() function or curly braces {}. A set() returns a set object from an iterable.

SET OPERATIONS:
A = {'data', 'structure','python'}
B = {'python', 'Java','C', 'data'}

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

IMMUTABLE SETS:
In Python, frozenset is another built-in type data structure, which is, in all respects, exactly 
like a set, except that it is immutable, and so cannot be changed after creation. The order of the 
elements is also undefined. A frozenset is created by using the built-in function frozenset():
x = frozenset(['data', 'structure', 'and', 'python'])

"""

A = {'data', 'structure','python'}
B = {'python', 'Java','C', 'data'}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.issubset(B))


x = frozenset(['data', 'structure', 'and', 'python'])
a1 = frozenset(['data'])
a2 = frozenset(['structure'])
a3 = frozenset(['python'])
x1 = {a1, a2, a3}
print(x1)
