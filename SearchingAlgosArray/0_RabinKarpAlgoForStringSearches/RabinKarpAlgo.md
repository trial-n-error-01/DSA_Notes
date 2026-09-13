# Rabin-Karp Algorithm

Rabin-Karp is a string-searching algorithm used to find a pattern inside a text using hashing.

## Idea

The algorithm computes the hash of the pattern and then compares it with the hash of every window of the same length in the text.

- If the hash matches, it may be a valid match.
- To be sure, it checks the actual characters.
- This helps avoid false matches caused by hash collisions.

## How it works

1. Compute the hash of the pattern.
2. Slide a window over the text of the same length as the pattern.
3. Compute the hash of each text window.
4. If the hash matches the pattern hash, compare the actual substring.
5. Continue until the end of the text.

## Example

Text: `GEEKSFORGEEKS`
Pattern: `GEEKS`

The algorithm hashes `GEEKS` and then checks each window in the text:

- `GEEKS` -> match
- `EEKSF` -> no match
- `EKSFO` -> no match
- ...
- eventually the pattern is found

## Why it is useful

Rabin-Karp is efficient when searching for a pattern in a large text, especially when using a rolling hash.

Instead of recomputing the hash of the entire window every time, the algorithm updates the previous hash as the window slides.

## Time Complexity

- Average case: O(n + m)
- Worst case: O(n × m)

Where:

- n = length of text
- m = length of pattern

## When does the worst case usually happen?

The worst case usually happens when many text windows produce the same hash value as the pattern hash, even when the actual strings are different.

This causes extra comparisons, because the algorithm must verify each matching hash by checking the real characters.

In simple terms:

- if hash collisions happen often,
- or the pattern and text have many similar-looking windows,
- then the algorithm may end up doing much more work than the average case.

This is why the worst case can become O(n × m).

## Space Complexity

- O(1) extra space (ignoring the input storage)

## Key point

The main idea is to use hashing so the algorithm can compare pattern and text windows quickly.

> Rabin-Karp is especially useful for multiple pattern matching and situations where rolling hash can be applied.

## Best Used For

- **Multiple Pattern Searching:** It can be easily extended to search for multiple patterns simultaneously in a text using a set or data structure (like a Bloom filter) of pattern hashes.
- **Plagiarism Detection:** Useful for finding matching blocks of text or code across large documents.

## Summary

Rabin-Karp is a fast string matching algorithm that uses hash values to compare a pattern against all text windows efficiently.
