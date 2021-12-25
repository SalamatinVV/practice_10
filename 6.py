def interpolation(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return interpolation(arr, lo, pos - 1, x)
    rerurn - 1


print(interpolation([1, 2, 3, 4, 5, 6], 3, 5, 4))
