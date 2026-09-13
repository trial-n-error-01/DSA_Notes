## String Concatenation Complexity

Suppose we want to concatenate `N` strings, and every string has the same length `X`.

The final string has length `N * X`.

### Repeated Concatenation

Consider this Java code:

```java
String joinWords(String[] words) {
 String sentence = "";

 for (String word : words) {
  sentence = sentence + word;
 }

 return sentence;
}
```

Java strings are immutable. Every time `sentence + word` runs, Java creates a new string and copies the existing characters and the new word into it.

The work grows on every iteration:

```text
Iteration 1: copy X characters
Iteration 2: copy 2X characters
Iteration 3: copy 3X characters
...
Iteration N: copy NX characters
```

The total work is:

$$
X + 2X + 3X + \cdots + NX
$$

Factor out `X`:

$$
X(1 + 2 + 3 + \cdots + N)
$$

The sum of the first `N` integers is:

$$
1 + 2 + \cdots + N = \frac{N(N+1)}{2} = O(N^2)
$$

Therefore, repeated string concatenation takes:

$$
O(XN^2)
$$

The `X` factor represents the length of each string, and the `N^2` factor comes from repeatedly copying the increasingly longer sentence.

## Java StringBuilder

`StringBuilder` is a mutable, resizable character array. It appends characters without creating a new string for every iteration.

```java
String joinWords(String[] words) {
 StringBuilder sentence = new StringBuilder();

 for (String word : words) {
  sentence.append(word);
 }

 return sentence.toString();
}
```

The append operation is **O(X) amortized** because each word contains `X` characters. Occasional resizing may copy the existing characters, but resizing happens infrequently.

The final `toString()` creates the completed string once, which costs O(XN). Therefore, the total complexity is:

$$
O(XN)
$$

This improves the repeated-concatenation solution from O(XN^2) to O(XN).

## Python Equivalent

Python strings are also immutable, so repeated concatenation has the same potential problem:

```python
def join_words(words):
 sentence = ""

 for word in words:
  sentence += word

 return sentence
```

In general, this can take:

$$
O(XN^2)
$$

### Python `join`

The usual Python solution is to collect the strings in a list and join them once:

```python
def join_words(words):
 parts = []

 for word in words:
  parts.append(word)  # O(1) amortized

 return "".join(parts)  # O(XN)
```

The complexity is:

- `list.append`: O(1) amortized per word
- `"".join`: O(XN), because the final string has `XN` characters
- Total: **O(XN)**

Python implementations such as CPython may optimize some `+=` cases, but this behavior should not be relied upon for general complexity analysis. `"".join(parts)` is the standard and reliable approach.

## Summary

| Approach | Complexity |
| --- | ---: |
| Repeated Java string concatenation | O(XN^2) |
| Java `StringBuilder` | O(XN) |
| Repeated Python string concatenation | O(XN^2) in general |
| Python list plus `join` | O(XN) |

The main lesson is to avoid repeatedly copying an immutable string when building a large result. Use a mutable builder or collect the parts and combine them once.
