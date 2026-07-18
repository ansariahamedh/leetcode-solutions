# Valid Anagram (#242)

## Pattern
Frequency Counting

## Data Structure
Dictionary

## Time Complexity
O(n)

## Space Complexity
O(n)

## Mistakes I Made
- Initially I only checked if characters existed.
- I forgot to count the frequency of characters.
- I returned inside the loop.
- I didn't know how to store counts in a dictionary.

## What I Learned
Use a dictionary to count the frequency of each character.

Pattern:

if key exists:
    increase count

else:
    create key with value 1

## Confidence
★★★★☆