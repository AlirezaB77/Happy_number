# Happy Number Checker

This Python function determines whether a given number is a "Happy Number".

## What is a Happy Number?

A Happy Number is defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy numbers.

## Function Description

```python
def happy_number(n):
    senn_number = set()
    while n != 1 and (n not in senn_number):
        senn_number.add(n)
        n = sum([int(i)**2 for i in str(n)])
    return n == 1
```

This function takes a positive integer `n` as input and returns `True` if it's a Happy Number, and `False` otherwise.

## How it works

1. We use a set `senn_number` to keep track of numbers we've seen in the process.
2. We continue the process until either:
   - The number becomes 1 (Happy Number)
   - We encounter a number we've seen before (not a Happy Number)
3. In each iteration, we calculate the sum of squares of digits.
4. The function returns `True` if the process ends with 1, and `False` otherwise.

## Usage

```python
print(happy_number(19))  # True
print(happy_number(4))   # False
```
