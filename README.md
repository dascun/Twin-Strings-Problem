# Twin-Strings-Problem
Here is a solution provided to the **twin strings** problem.

## Problem Description
Two strings, *a* and *b*, are said to be *twins* only if they can be made equivalent by performing some number of operations on one or both strings. There are two possible operations:

- *SwapEven*: Swap a character at an even-numbered index with a character at another even-numbered index.
- *SwapOdd*: Swap a character at an odd-numbered index with a character at another odd-numbered index.

For example, *a = "abcd"* and *b = "cdab"* are twins because we can make them equivalent by performing operations. Alternatively, *a = "abcd"* and *b = "bcda"* are not twins (operations do not move characters between odd and even indices), and neither are *a = "abc"* and *b = "ab"* (no amount of operations will insert a *'c'* into string *b*).

Complete the *twins* function in the provided code. It has two parameters:

1. An array of *n* strings named *a*.
2. An array of *n* strings named *b*.

The function must return an array of strings where each index *i* (*0 ≤ i < n*) contains the string Yes if *ai* and *bi* are twins or the string No if they are not.

**Input Format**

The provided code reads the following input from stdin and passes it to the function:
The first line contains an integer, *n*, denoting the number of elements in *a*.
Each line *i* of the *n* subsequent lines (where *0 ≤ i < n*) contains a string describing *ai*.
The next line contains an integer, *n*, denoting the number of elements in *b*.
Each line *i* of the *n* subsequent lines (where *0 ≤ i < n*) contains a string describing *bi*.

**Constraints**

- *1 ≤ n ≤ 10^3*
- *1 ≤ lengths of ai, bi ≤ 100*
- *ai* and *bi* are *not* guaranteed to have the same length.
- Strings *ai* and *bi* contain lowercase letters only (i.e., *a* through *z*).
 
**Output Format**

The function must return an array of strings where each index *i* (*0 ≤ i < n*) contains the string Yes if *ai* and *bi* are twins or the string No if they are not.

**Sample Input 0**

2
cdab
dcba
2
abcd
abcd

**Sample Output 0**

Yes
No

**Explanation 0**

Given *a = ["cdab", "dcba"]* and *b = ["abcd", "abcd"]*, we process each element like so:
1. *a0 = "cdab"* and *b0 = "abcd"*: We store Yes in index 0 of the return array because *a0 = "cdab" → "adcb" → "abcd" = b0*.
2. *a1 = "dcba"* and *b1 = "abcd"*: We store No in index *1* of the return array because no amount of operations will move a character from an odd index to an even index, so the two strings will never be equal.
We then return the array *["Yes", "No"]* as our answer.
