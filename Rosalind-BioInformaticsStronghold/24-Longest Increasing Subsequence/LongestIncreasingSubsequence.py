def longest_increasing_subsequence(arr):
    from bisect import bisect_left

    # Initialize a list to store the smallest ending element of the increasing subsequences
    lis = []
    # To track the indices for reconstruction
    indices = [-1] * len(arr)
    prev_index = [-1] * len(arr)

    for i, value in enumerate(arr):
        pos = bisect_left(lis, value)
        # If pos is equal to the length of lis, this means we found a new longer subsequence
        if pos == len(lis):
            lis.append(value)
        else:
            lis[pos] = value
        indices[pos] = i
        if pos > 0:
            prev_index[i] = indices[pos - 1]

    # Reconstruct the longest increasing subsequence
    longest_increasing = []
    k = indices[len(lis) - 1]
    while k >= 0:
        longest_increasing.append(arr[k])
        k = prev_index[k]
    return longest_increasing[::-1]  # Return in the correct order


def longest_decreasing_subsequence(arr):
    # To find the LDS, we can find the LIS of the reversed array
    return longest_increasing_subsequence(arr[::-1])[::-1]  # Reverse the result


def find_longest_subsequences(n, permutation):
    lis = longest_increasing_subsequence(permutation)
    lds = longest_decreasing_subsequence(permutation)
    return lis, lds


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        # Read the first line for n (though we don't need to use n directly)
        n = int(file.readline().strip())
        # Read the second line for the permutation
        permutation = list(map(int, file.readline().strip().split()))
    return n, permutation