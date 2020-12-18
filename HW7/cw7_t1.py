def count_positives_sum_negatives(arr):
    if arr == []: return []
    a = 0
    b = 0
    for i in arr:
        if i>0:
            a+=1
        if i<0:
            b+=i
    return [a, b]