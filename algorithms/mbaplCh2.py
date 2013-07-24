# -*- encoding: UTF-8 -*-
"""Python Algorithms-Mastering Basic Algorithms in the Python Language
CHAPTER 2 The Basics
"""
try:
    inf = float('inf')
except:  # check for a particular exception here?
    inf = 1e30000
class Node(object):
    """Node of a so-called singly linked list"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


"""Common Examples of Asymptotic Running Times
O(1)     Constant          Hash table lookup and modification
O(lgn)   Logarithmic       Binary Search
O(n)     Linear            Iterating over a list
O(nlgn)  Loglinear         Optimal sorting of arbitrary values
O(n**2)  Quadratic         Comparing n objects to each other
O(n**3)  Cubit             Floyd and Warshall's algorithms
O(n**k)  Polynomial        k nested for loops over n
O(k**n)  Exponential       Producing every subset of n items
O(n!)    Factorial         Producing every ordering of n values
"""
"""Code examples:
nums is a list of size n
$> nums.append(1)               O(1)
$> nums.insert(0, 2)            O(n+1) == O(n)
Result:                         O(n) + O(1) == O(n)

Some linear running time example:
$> s = 0
$> for x in seq:
$>     s += x
$> squares = [x**2 for x in seq]

O(n**2):
$> s = 0
$> for x in seq:
$>     for y in seq:
$>         s += x*y

O(n(n + n**2)) = O(n**2 + n**3) = O(n**3)
$> s = 0
$> for x in seq:
$>     for y in seq:
$>         s += x*y
$>     for z in seq:
$>         for w in seq:
$>             s += x-w
"""


# A Weight Matrix with Infinite Weight
a, b, c, d, e, f, g, h = range(8)
_ = float('inf')
W = [[0, 2, 1, 3, 9, 4, _, _],
     [_, 0, 4, _, 3, _, _, _],
     [_, _, 0, 8, _, _, _, _],
     [_, _, _, 0, 7, _, _, _],
     [_, _, _, _, 0, 5, _, _],
     [_, _, 2, _, _, 0, 2, 2],
     [_, _, _, _, _, 1, 0, 6],
     [_, _, _, _, _, 9, 8, 0]]


class Tree(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Tree2(object):
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next


if __name__ == '__main__':
    L = Node("a", Node("b", Node("c", Node("d"))))
    print L.next.next.value
    import timeit
    print timeit.timeit("x = 2 + 2")
    print timeit.timeit("x = sum(range(10))")
    assert W[a][b] < inf
    assert W[c][e] == inf
    print sum(1 for w in W[a] if w < inf) - 1
    t = Tree(Tree("a", "b"), Tree("c", "d"))
    print t.right.left
    t = Tree2(Tree2("a", Tree2("b", Tree2("c", Tree2("d")))))
    t.kids.next.next.val
    print t.kids.kids
