def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append remaining elements
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# Example usage:
left_half = [2, 4, 6]
right_half = [1, 3, 5]
merged_list = merge(left_half, right_half)
print("Merged list is:", merged_list)
