def rabin_karp_search(text, pattern):
    """
    Returns all starting indices where pattern occurs in text.
    Uses a simple rolling hash approach.
    """
    if pattern == "":
        return [0]

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    base = 256  # number of possible characters
    mod = 101  # small prime to keep hash manageable

    # Compute initial hash values
    pattern_hash = 0
    text_hash = 0
    print(f"\nPattern = '{pattern}'")
    print(f"Text = '{text}'")
    print(f"Window size = {m}")
    print("\nStep 1: Compute hash for the first window of text and the pattern")

    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        text_hash = (text_hash * base + ord(text[i])) % mod

    print(f"Initial pattern hash = {pattern_hash}")
    print(f"Initial text window '{text[0:m]}' hash = {text_hash}")

    result = []

    # Slide through the text
    print("\nStep 2: Compare each window using rolling hash")
    for i in range(n - m + 1):
        current_window = text[i:i + m]
        print(f"\nChecking window at index {i}: '{current_window}'")
        print(f"Current text window hash = {text_hash}")
        print(f"Pattern hash = {pattern_hash}")

        if text_hash == pattern_hash:
            print(f"Hash matches at index {i}. Now checking actual string equality...")
            if current_window == pattern:
                print(f"Exact match found! Appending index {i}")
                result.append(i)
            else:
                print("Hash collision detected: same hash, but different string.")
        else:
            print("Hash does not match. Moving to next window.")

        if i < n - m:
            # Roll hash: remove leftmost char and add next char
            print("Updating hash for next window...")
            old_char = text[i]
            new_char = text[i + m]
            text_hash = (text_hash - ord(old_char) * (base ** (m - 1))) % mod
            text_hash = (text_hash * base + ord(new_char)) % mod
            print(f"Removed '{old_char}', added '{new_char}', new hash = {text_hash}")

    print(f"\nFinal result: {result}")
    return result


# Example from the notes
text = "GEEKSFORGEEKS"
pattern = "GEEKS"

positions = rabin_karp_search(text, pattern)
print(f"Text: {text}")
print(f"Pattern: {pattern}")
print(f"Pattern found at indices: {positions}")
