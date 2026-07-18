# Contains Duplicate (#217)

## Pattern

Hash Set

## Idea

Create an empty set.

Loop through every number.

- If the number is already in the set, return True.
- Otherwise, add it to the set.

If the loop finishes without finding duplicates, return False.

## Time Complexity

O(n)

Reason:
We visit each element once.
Set lookup and insertion are O(1) on average.

## Space Complexity

O(n)

Reason:
In the worst case, the set stores every unique element.