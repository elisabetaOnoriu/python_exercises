def merge_sort(elements):
    if len(elements) <= 1:
        return elements

    mid = len(elements) // 2
    left_half = merge_sort(elements[:mid])
    right_half = merge_sort(elements[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Get input and convert to integers
given_elements = input("Enter comma-separated numbers to sort: ").split(", ")
given_elements = [int(x) for x in given_elements]

sorted_elements = merge_sort(given_elements)
print("Sorted elements:", sorted_elements)
