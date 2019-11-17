
# Binary search tree (BST)

<http://techieme.in/count-binary-search-trees/>

## Properties

1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
1. The right subtree of a node contains only nodes with keys greater than the node’s key.
1. The left and right subtree each must also be a binary search tree. There must be no duplicate nodes.

How many Binary Search Trees are possible for a given **set** of N elements?

We will take as an example the following set of numbers $6, 10, 13, 5, 8, 3, 2, 11$

Questions

1. Question 1: Do we know the answer for N = 0?
1. Question 2: Do we know the answer for N = 1?
1. Question 3: Do we know the answer for N = 2?
1. Question 4: Is there any relation of pattern?
1. Question 5: Is there a solution for N = i which can contribute to the solution of N = k where i < k ?

1. Answer 1: When N = 0 then there is no tree or I can say an empty tree, hence total number of possible BSTs is 1
1. Answer 2: When N = 1 then there is only one tree, and that is the root as below, so the number of trees = 1
1. Answer 3: When N = 2 then there are two trees possible:
    1. With 6 as root and
    1. With 10 as root
    1. So the number of trees = 2
1. Answer 4: When N = 3 then we will have following options:
    1. With 6 as root
    1. With 10 as root and
    1. With 13 as root.

Then we see that when 6 is the root then 10 and 13 lie on the right side of the root. That means there are as many possibilities as we had with N = 2 same as the Answer 3.

Similarly when 10 is the root, 6 lies in the left and 13 on the right of the root. So, we have those many possibilities on each side as many we had when N = 1 same as the Answer 2. BUt we must also realize that for each possibility of left we can have all the possibility in the right or vice versa. In simple words the number of trees formed from the elements in the right is independent of the number of trees formed from the elements in the right. So the total number of trees will be a product of the total left trees and total right trees.

To explain it more, for each tree of the left we can have all possible trees in the right.

Similarly when 13 is the root, 6 and 10 lie on the left side of the root, Than means there are as many possibilities as we had with N = 2 same as Answer 3.

Hence total number of trees possible is 2 + 1 * 1 + 2 = 5. So there is a pattern.

Number of BSTs for four distinct elements, lets say $1, 2, 3, 4$

p stands for possibility/possibilities

1. (0 p) [] **1** [2, 3, 4] (5 p) = 1 x 5 p
1. (1 p)[1] **2** [3, 4] (2 p) = 1 x 2 p
1. (2 p)[1, 2] **3** [4] (1 p) = 2 x 1 p
1. (5 p) [1, 2, 3] **4** [] (0 p) = 5 x 1 p

Total BST for four distinct elements = 5 + 2 + 2 + 5 = 14

Number of BSTs for five distinct elements, lets say $1, 2, 3, 4, 5$

1. $(0 p) [] **1** [2, 3, 4, 5] (14 p) = 1 x 14 p$
1. (1 p)[1] **2** [3, 4, 5] (5 p) = 1 x 5 p
1. (2 p)[1, 2] **3** [4, 5] (2 p) = 2 x 2 p
1. (5 p) [1, 2, 3] **4** [5] (1 p) = 5 x 1 p
1. (14 p) [1, 2, 3, 4] **5** [] (1 p) = 14 x 1 p

Total BST for five distinct elements = 14 + 5 + 4 + 5 + 14 = 42
