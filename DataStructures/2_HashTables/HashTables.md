## Hash Tables

A hash table (also known as a hash map) is a data structure used to store and organize information in key-value pairs. It allows for extremely fast data retrieval, insertion, and deletion, regardless of the amount of data stored.

**key-value pairs**.

```text
"name" -> "Alice"
"age"  -> 25
```

A **hash function** converts a key into an array index:

```text
hash("name") -> 3
```

The value can then be found quickly by using that index.

### Common Complexities

| Operation | Average case | Worst case |
| --- | ---: | ---: |
| Insert | O(1) | O(N) |
| Search | O(1) | O(N) |
| Delete | O(1) | O(N) |

Average O(1) performance assumes a good hash function and a controlled load factor.

### Why the Worst Case Is O(N)

The worst-case O(N) occurs when many keys produce the same array index. This is called a collision.

For example, if all `N` entries hash to index `3`, separate chaining might look like this:

```text
Index 3 -> key1 -> key2 -> key3 -> ... -> keyN
```

In this situation:

- A search may need to check all `N` entries: **O(N)**
- A delete may need to search through all `N` entries first: **O(N)**
- An insert may need to check all `N` entries before adding a new key: **O(N)**

With open addressing, a collision can also force the table to probe through up to `N` occupied positions. Insertion can additionally be O(N) when the table resizes and rehashes all existing entries.

Therefore:

- Average case: keys are spread across buckets, so operations are **O(1)**.
- Worst case: keys cluster together, so operations may scan many entries and become **O(N)**.

## Collisions

A **collision** occurs when two different keys produce the same array index:

```text
hash("Alice") -> 3
hash("Bob")   -> 3
```

Both keys cannot occupy the same position directly, so the hash table must use a collision-resolution technique.

### Separate Chaining

With separate chaining, each array position stores a collection of entries, often a linked list:

```text
Index 3 -> ("Alice", 25) -> ("Bob", 30)
```

Both entries are stored at index `3`.

- Average insert, search, and delete: **O(1)**
- Worst case: **O(N)** if many keys collide
- Deletion is straightforward
- Requires extra memory for the collections

**Advantages**: It is simple to implement, handles high data loads gracefully, and performance degrades linearly rather than catastrophically as the table fills.


**Disadvantages**: It requires extra memory overhead for pointers, and worst-case lookup time drops if a single chain becomes overly long.


### Open Addressing

With open addressing, all entries are stored directly inside the hash table array. If the calculated position is occupied, the table probes other positions until it finds an available one.

#### Linear Probing

Linear probing checks the next positions one at a time:

```text
index 3 -> occupied
index 4 -> occupied
index 5 -> available
```

The new entry is stored at index `5`.

- Simple and cache-friendly
- Can create clusters of occupied positions
- Deletion may require a special marker called a **tombstone**

#### Quadratic Probing

Quadratic probing checks positions using increasingly larger jumps:

```text
index + 1^2
index + 2^2
index + 3^2
```

For an original index of `3`, the table might check positions `3`, `4`, `7`, and `12`.

- Reduces clustering compared with linear probing
- May not visit every position unless the table is configured carefully

#### Double Hashing

Double hashing uses a second hash function to calculate the jump size:

```text
next index = hash1(key) + attempt * hash2(key)
```

- Usually distributes entries better
- Reduces clustering
- Requires two well-designed hash functions

## Load Factor

The **load factor** measures how full a hash table is:

```text
load factor = number of entries / table capacity
```

For example, a table with `7` entries and a capacity of `10` has a load factor of `0.7`.

As the load factor increases, collisions become more likely. Hash tables usually resize and rehash their entries when the load factor becomes too high.

With a good hash function and a controlled load factor:

- Average operations remain **O(1)**
- Worst-case operations remain **O(N)**

## Examples in Programming Languages

- Python: `dict`
- Java: `HashMap`
- JavaScript: `Map`
- C++: `unordered_map`
