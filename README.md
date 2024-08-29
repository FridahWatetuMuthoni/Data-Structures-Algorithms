# Data Structures and Algorithms

## Data Structures

Data structures deal with how the data is stored and organized in the memory of the computer that is going to be used in a program. Computer scientists should understand how efficient
an algorithm is and which data structure should be used in its implementation.

## Algorithms

An algorithm is essentially a step-by-step set of instructions to be followed by a computer system, to solve the problem. An algorithm can be converted into computer software using any programming language.

## Performance analysis of an algorithm

The performance of an algorithm is generally measured by the size of its input data, n, and the time and the memory space used by the algorithm. The time required is measured by the key operations to be performed by the algorithm (such as comparison operations), where key operations are instructions that take a significant amount of time during execution. Whereas the space requirement of an algorithm is measured by the memory needed to store the variables, constants, and instructions during the execution of the program.

### Time Complexity

The time complexity of the algorithm is the amount of time that an algorithm will take to execute on a computer system to produce the output.
The aim of analyzing the time complexity of the algorithm is to determine, for a given problem and more than one algorithm, which one of the algorithms is the most efficient with respect to the time required to execute. The running time required by an algorithm depends on the input size; as the input size, n, increases, the runtime also increases. Input size is measured as the number of items in the input, for example, the input
size for a sorting algorithm will be the number of items in the input. So, a sorting algorithm will have an increased runtime to sort a list of input size 5,000 than that of a list of input size 50.
The runtime of an algorithm for a specific input depends on the key operations to be executed in the algorithm. For example, the key operation for a sorting algorithm is a comparison operation that will take up most of the runtime, compared to assignment or any other operation. Ideally, these key operations should not depend upon the hardware, the operating system, or the programming language being used to implement the algorithm.

```python
if n == 0 || n == 3: #c1
    print('data') #c2
else:
    for i in range(n): #c4
        print('structire') #c5

```

T(n) = c1 + c3 + c4 x n + c5 x n
T(n) = c1 + c2

```python

def linear_search(input_lits, element):
    for index, value in emumerate(input_list):
        if value == element:
            return index

input_list = [3, 4, 1, 6, 14]
element = 4
print(linear_search(input_list, element))
```

Average running time calculation
T(n) = n(n+1) / 2n

### Space complexity

The space complexity of the algorithm estimates the memory requirement to execute it on a computer to produce the output as a function of input data. The memory space requirement of an algorithm is one of the criteria used to decide how efficient it is. While executing the algorithm
on the computer system, storage of the input is required, along with intermediate and temporary data in data structures, which are stored in the memory of the computer. In order to write a programming solution for any problem, some memory is required for storing variables, program
instructions, and executing the program on the computer. The space complexity of an algorithm is the amount of memory required for executing and producing the result.

### Asymptotic notation

To analyze the time complexity of an algorithm, the rate of growth (order of growth) is very important when the input size is large. When the input size becomes large, we only consider the higher-order terms and ignore the insignificant terms. In asymptotic analysis, we analyze the efficiency of algorithms for large input sizes considering the higher order of growth and ignoring the multiplicative constants and lower-order terms.
The following asymptotic notations are commonly used to calculate the running time complexity of an algorithm:
• θ notation: It denotes the worst-case running time complexity with a tight bound.
• Ο notation: It denotes the worst-case running time complexity with an upper bound, which ensures that the function never grows faster than the upper bound.
• Ω notation: It denotes the lower bound of an algorithm’s running time. It measures the best amount of time to execute the algorithm.

### Big O notation

O(1) => constant
O(log n) => logarithmic => increases by one each time the data is doubled
O(n) => linear
O(n log n) => linear logarithic
O(n2) => quadratic
O(n3) =>cubic
O(2n)=> exponential

To excel in programming interviews, it's crucial to have a solid understanding of common data structures, as they're often used to solve problems efficiently. Here's a list of data structures you should focus on:

### Basic Data Structures

1. **Arrays**: Understanding how to work with fixed-size collections of elements, indexing, and common operations (insertion, deletion, traversal).
2. **Strings**: Although technically arrays of characters, string-specific algorithms and manipulation techniques are essential.
3. **Linked Lists**: Master both singly and doubly linked lists, including operations like insertion, deletion, reversal, and searching.
4. **Stacks**: Learn about LIFO (Last In, First Out) operations and their applications in problems like balancing parentheses, backtracking, etc.
5. **Queues**: Understand FIFO (First In, First Out) operations, including variations like circular queues and priority queues.
6. **Hash Tables**: Learn how to implement hash tables, handle collisions, and their use cases in fast lookups and storage.

### Intermediate Data Structures

1. **Trees**:

   - **Binary Trees**: Understand tree traversal methods (in-order, pre-order, post-order).
   - **Binary Search Trees (BST)**: Focus on insertion, deletion, and searching.
   - **AVL Trees**: Learn about self-balancing trees and their operations.
   - **Heaps**: Understand both min-heaps and max-heaps, and their use in priority queues.

2. **Graphs**:

   - **Graph Representation**: Learn about adjacency lists and adjacency matrices.
   - **Graph Traversal**: Master Breadth-First Search (BFS) and Depth-First Search (DFS).
   - **Topological Sorting**: Understand how to sort nodes of a Directed Acyclic Graph (DAG).
   - **Shortest Path Algorithms**: Learn about Dijkstra's and Bellman-Ford algorithms.

3. **Tries (Prefix Trees)**: Used for efficient retrieval of keys in datasets of strings. Useful for autocomplete and spell-checking applications.

### Advanced Data Structures

1. **Segment Trees**: Useful for range query problems, like finding the sum or minimum in a range.
2. **Fenwick Trees (Binary Indexed Trees)**: Similar to segment trees but often simpler to implement.
3. **Disjoint Set (Union-Find)**: Used to track a set of elements partitioned into disjoint (non-overlapping) subsets, crucial for network connectivity problems.
4. **Red-Black Trees**: Self-balancing BSTs that ensure balanced tree height for guaranteed logarithmic operations.
5. **B-Trees**: Balanced tree data structure that generalizes the binary search tree, often used in databases and file systems.

### Practice and Implementation Tips

- **Learn the Concepts**: Understand each data structure's properties, advantages, and disadvantages.
- **Implement From Scratch**: Writing your own implementations helps solidify your understanding.
- **Solve Problems**: Practice problems using these data structures on platforms like LeetCode, HackerRank, or CodeSignal.
- **Analyze Complexity**: Be comfortable with the time and space complexity of operations associated with each data structure.

To excel in programming interviews, it's essential to have a strong grasp of a variety of algorithms. These algorithms are frequently used to solve common interview problems efficiently. Here's a comprehensive list of algorithms you should learn:

### 1. **Sorting Algorithms**

- **Bubble Sort**: Understand its simplicity and inefficiency for large datasets.
- **Selection Sort**: Learn how it repeatedly selects the minimum element.
- **Insertion Sort**: Grasp its effectiveness for small or nearly sorted datasets.
- **Merge Sort**: A classic example of divide and conquer; important for its stable sort properties.
- **Quick Sort**: Another divide and conquer algorithm, notable for its efficiency and average-case performance.
- **Heap Sort**: Based on binary heaps, this is important for understanding priority queues.
- **Counting Sort**: A non-comparison-based algorithm useful for small integer ranges.
- **Radix Sort**: A non-comparison-based sorting algorithm for integers and strings.

### 2. **Searching Algorithms**

- **Linear Search**: Basic search method; useful for unsorted data.
- **Binary Search**: Efficient search method for sorted data; understand how it divides the search space in half.
- **Depth-First Search (DFS)**: Important for graph traversal, finding connected components, and solving maze problems.
- **Breadth-First Search (BFS)**: Useful for shortest-path problems on unweighted graphs and graph traversal.

### 3. **Dynamic Programming (DP)**

- **Understanding DP Concepts**: Master memoization and tabulation.
- **Fibonacci Sequence**: Classic DP example for understanding overlapping subproblems.
- **Knapsack Problem**: Understand both 0/1 knapsack and fractional knapsack.
- **Longest Common Subsequence (LCS)**: Useful for DNA sequence analysis, diff utilities.
- **Longest Increasing Subsequence (LIS)**: Important for sequence alignment and array problems.
- **Edit Distance (Levenshtein Distance)**: Measures similarity between two strings.
- **Matrix Chain Multiplication**: Classic DP optimization problem.
- **Coin Change Problem**: Learn both the minimum number of coins and the number of ways to make a certain amount.

### 4. **Graph Algorithms**

- **Dijkstra's Algorithm**: Find the shortest path in weighted graphs.
- **Bellman-Ford Algorithm**: Handle graphs with negative weights.
- **Floyd-Warshall Algorithm**: Find shortest paths between all pairs of nodes.
- **Kruskal's Algorithm**: Minimum spanning tree (MST) using the disjoint-set data structure.
- **Prim's Algorithm**: Another approach to find the MST of a graph.
- **Topological Sorting**: Order vertices in a Directed Acyclic Graph (DAG).
- **A\* Search Algorithm**: Used in pathfinding and graph traversal.

### 5. **Greedy Algorithms**

- **Activity Selection**: Selecting the maximum number of activities without overlapping.
- **Huffman Coding**: A greedy algorithm for data compression.
- **Dijkstra’s Algorithm**: Although it's a graph algorithm, it’s greedy in nature.
- **Job Sequencing Problem**: Maximize profit for job scheduling.

### 6. **Backtracking Algorithms**

- **N-Queens Problem**: Classic example of placing N queens on an N×N chessboard.
- **Sudoku Solver**: Filling the grid by following the game's constraints.
- **Permutations and Combinations**: Generate all permutations of a set or string.
- **Subset Sum Problem**: Find subsets that sum up to a target value.
- **Rat in a Maze**: Find paths for a rat to reach the end of a maze.

### 7. **Divide and Conquer Algorithms**

- **Merge Sort**: Dividing array into halves, sorting, and merging.
- **Quick Sort**: Choosing a pivot and partitioning the array around it.
- **Binary Search**: Searching in a sorted array by dividing the search space.
- **Closest Pair of Points**: Finding the closest pair in a set of points.

### 8. **Mathematical Algorithms**

- **Greatest Common Divisor (GCD)**: Using Euclid’s algorithm.
- **Sieve of Eratosthenes**: Efficiently finding all prime numbers up to a given limit.
- **Exponentiation by Squaring**: Efficiently compute large powers.
- **Counting Inversions**: Count the number of inversions in an array using a modified merge sort.
- **Fast Fourier Transform (FFT)**: For polynomial multiplication.

### 9. **String Algorithms**

- **KMP (Knuth-Morris-Pratt)**: Efficient pattern matching.
- **Rabin-Karp Algorithm**: String matching using hashing.
- **Trie-based Algorithms**: For efficient storage and retrieval of strings.
- **Z Algorithm**: Linear time string matching algorithm.
- **Manacher’s Algorithm**: Finding the longest palindromic substring in linear time.

### 10. **Bit Manipulation**

- **Basic Bit Operations**: AND, OR, XOR, NOT, shifts.
- **Counting Set Bits**: Using Brian Kernighan’s algorithm.
- **Finding the Only Non-Repeating Element**: XOR-based solutions.
- **Power of Two Check**: Check if a number is a power of two using bits.

### 11. **Miscellaneous Algorithms**

- **Reservoir Sampling**: Random sampling from a stream of unknown size.
- **Fisher-Yates Shuffle**: Efficient algorithm for shuffling an array.
- **Union-Find Algorithm**: For handling dynamic connectivity queries.
- **Bloom Filters**: Probabilistic data structure for set membership queries.
- **Sliding Window Technique**: Efficiently finding subarray problems.
- **Two-Pointer Technique**: Efficiently solving problems on arrays and strings.
