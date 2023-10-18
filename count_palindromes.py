print("Hello world")


def is_valid_palindrom(l, r):
    count = 0
    while l < r:
        if s[l] == s[r]:
            count += 1
        l -= 1
        r += 1
    return count


def count_palindromes(s):
    res = 0
    for k in range(len(s)):
        # for odd palindromes
        l, r = k, k
        res += is_valid_palindrom(i, i)

        # for even palindromes
        l, r = k, k + 1
        res += is_valid_palindrom(l, r)
    return res

# time complexity O(n^2)
# space complexity is O(1)
