# 1. To find the maximum sum of all subarrays of size K:
# Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
#
# Input  : arr[] = {100, 200, 300, 400}, k = 2
# Output : 700
#
#
# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.
#
#
# Input  : arr[] = {2, 3}, k = 3
# Output : Invalid
# There is no subarray of size 3 as size of whole array is 2.

def max_sum(arr,k):
    n = len (arr)
    current_sum = 0
    if k>n:
        return "Invalid"
    for i in range(0,k):
        current_sum += arr[i]
    highest_sum = current_sum






arr = [4, 2, 1, 7, 3, 8, 9, 0, 6]
k = 3
print(max_sum(arr, k))