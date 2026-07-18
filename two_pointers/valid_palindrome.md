# Valid Palindrome (#125)

## Pattern
Two Pointers

## Data Structure
String

## Algorithm
1. Start left pointer at beginning.
2. Start right pointer at end.
3. Skip non-alphanumeric characters.
4. Convert both characters to lowercase.
5. Compare them.
6. If different → False.
7. Otherwise move both pointers inward.
8. Return True.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Mistakes I Made
- First thought about comparing halves.
- Forgot to handle special characters.
- Didn't know about `isalnum()`.
- Initially made a typo with `right -= 1`.

## What I Learned
When comparing from both ends of a string, think about the Two Pointer pattern.