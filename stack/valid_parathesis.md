# Valid Parentheses (#20)

## Pattern
Stack

## Data Structure
List (used as a stack)

## Algorithm
1. Create an empty stack.
2. Read each character.
3. If it's an opening bracket, push it.
4. If it's a closing bracket:
   - If stack is empty → False.
   - If top doesn't match → False.
   - Otherwise pop.
5. At the end, return True only if the stack is empty.

## Time Complexity
O(n)

Reason:
We traverse the string once, and each stack operation is O(1).

## Space Complexity
O(n)

Reason:
In the worst case, all opening brackets are stored in the stack.

## Mistakes I Made
(Your own notes)

## What I Learned
A stack follows Last In, First Out (LIFO).