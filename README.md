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

## Abstract Data Types

An abstract data type is a set of behaviours that we define a certain data type to have so that we can even call it that data type. e.g. for a stack, we need to support push and pop.
