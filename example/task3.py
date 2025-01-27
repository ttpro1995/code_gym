def count_splits(S):
    count_x = 0
    count_y = 0
    left_part_counts = {}
    total_splits = 0

    # Count 'x' and 'y' in the entire string
    for char in S:
        if char == 'x':
            count_x += 1
        elif char == 'y':
            count_y += 1

    # Initialize counts for the left part
    left_x = 0
    left_y = 0

    # Iterate through the string to count valid splits
    for i in range(len(S) - 1):
        if S[i] == 'x':
            left_x += 1
        elif S[i] == 'y':
            left_y += 1

        right_x = count_x - left_x
        right_y = count_y - left_y

        if left_x == left_y or right_x == right_y:
            total_splits += 1

    return total_splits

# Test cases
print(count_splits("ayxbx"))  # Expected output: 3
print(count_splits("xzzzy"))  # Expected output: 0
print(count_splits("toyxmy")) # Expected output: 5
print(count_splits("apple"))  # Expected output: 4
