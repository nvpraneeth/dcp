# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

k = 18
arr = [1,2,4,5,7,3,4,6,1,2,9,10,9,0,8]


def check_elem_sum(k, arr):
    for ele in arr:
        if not ele > k:
            k_diff = k - ele
            if k_diff in arr:
                return True
    return False


print(check_elem_sum(k, arr))

def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

print(two_sum(arr,k))
