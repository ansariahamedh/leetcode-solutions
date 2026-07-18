# Group Anagrams (#49)

## Pattern
Hash Map (Dictionary)

## Difficulty
Medium

---

## Problem

Given an array of strings `strs`, group the anagrams together.

### Example

Input:

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

Output:

```python
[
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]
```

---

# Key Idea

Two words are anagrams if they contain the same letters.

Sort each word alphabetically.

The sorted word becomes the dictionary key.

Example:

```text
eat → aet
tea → aet
ate → aet

tan → ant
nat → ant

bat → abt
```

Dictionary:

```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Return:

```python
list(groups.values())
```

---

# Algorithm

1. Create an empty dictionary.
2. Loop through every word.
3. Sort the word.
4. Convert the sorted characters into a string.
5. If the key exists:
   - Append the word.
6. Otherwise:
   - Create a new list with the word.
7. Return all dictionary values.

---

# Python Functions Used

## Sort

```python
sorted(word)
```

Example:

```python
sorted("eat")
```

Output:

```python
['a', 'e', 't']
```

---

## Join

```python
"".join(sorted(word))
```

Example:

```python
"".join(sorted("eat"))
```

Output:

```python
"aet"
```

---

## Dictionary Operations

Create dictionary

```python
groups = {}
```

Check key

```python
if key in groups:
```

Access value

```python
groups[key]
```

Create new key

```python
groups[key] = [word]
```

Append

```python
groups[key].append(word)
```

Return answer

```python
list(groups.values())
```

---

# Dry Run

Input

```python
["eat","tea","tan","ate","nat","bat"]
```

Processing

```text
eat → aet
tea → aet
tan → ant
ate → aet
nat → ant
bat → abt
```

Dictionary

```python
{
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"],
    "abt": ["bat"]
}
```

Return

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

# Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())
```

---

# Complexity Analysis

### Time Complexity

Sorting each word takes **O(k log k)**.

For **n** words:

**O(n × k log k)**

where:

- n = number of words
- k = average length of each word

---

### Space Complexity

Dictionary stores every word.

**O(n × k)**

---

# Common Mistakes

### ❌ Using quotes around the variable

Wrong

```python
sorted("word")
```

Correct

```python
sorted(word)
```

---

### ❌ Creating key outside the loop

Wrong

```python
key = "".join(sorted(word))

for word in strs:
```

Correct

```python
for word in strs:
    key = "".join(sorted(word))
```

---

### ❌ Forgetting join()

Wrong

```python
key = sorted(word)
```

Correct

```python
key = "".join(sorted(word))
```

---

### ❌ Using append on a dictionary

Wrong

```python
groups.append[key]
```

Correct

```python
groups[key] = [word]
```

---

### ❌ Storing a string instead of a list

Wrong

```python
groups[key] = word
```

Correct

```python
groups[key] = [word]
```

---

### ❌ Appending after creating a new key

Wrong

```python
groups[key] = [word]
groups[key].append(word)
```

Correct

```python
groups[key] = [word]
```

---

# Revision Points

- Sort every word.
- Use the sorted word as the dictionary key.
- Store original words as values.
- `sorted()` returns a list.
- `join()` converts the list to a string.
- Use `groups[key].append(word)` if the key exists.
- Use `groups[key] = [word]` for a new key.
- Return `list(groups.values())`.

---

## Pattern Learned

✅ Hash Map

## Related Problems

- Contains Duplicate (#217)
- Two Sum (#1)
- Valid Anagram (#242)
- Top K Frequent Elements (#347)