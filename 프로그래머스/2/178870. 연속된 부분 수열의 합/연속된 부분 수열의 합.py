def solution(sequence, k):
    n = len(sequence)
    left = 0
    current = 0

    best_len = n + 1
    ans = [0, 0]

    for right in range(n):
        current += sequence[right]

        while current > k and left <= right:
            current -= sequence[left]
            left += 1
        if current == k:
            curr_len = right - left + 1
            if curr_len < best_len:
                best_len = curr_len
                ans = [left, right]

    return ans
