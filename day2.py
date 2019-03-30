# Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

from functools import reduce
inp_arr = [4,5,6,1]
inp_set = set(inp_arr)
rslt = []
for val in inp_arr:
    rem_set = inp_set.difference(set([val]))
    rslt.append(reduce((lambda x, y: x * y), rem_set))

print("input")
print(inp_arr)
print("rslt")
print(rslt)

# method 2

mul_rslts_prev ={}
mul_rslts_post = {}
prev_val = None
for val in inp_arr:
    prev_mul = mul_rslts_prev.get(prev_val, 1)
    if not prev_val:
        prev_val = 1
    calc = prev_mul * prev_val
    mul_rslts_prev[val] = calc
    prev_val = val

inp_len = len(inp_arr)

prev_val = None
for idx2 in range(inp_len-1, -1, -1):
    val = inp_arr[idx2]
    post_mul = mul_rslts_post.get(prev_val, 1)
    if not prev_val:
        prev_val = 1
    calc = post_mul * prev_val
    mul_rslts_post[val] = calc
    prev_val = val

# print("prev")
# print(mul_rslts_prev)
# print("post")
# print(mul_rslts_post)

rslt = []
for val in inp_arr:
    rslt.append(mul_rslts_prev.get(val) * mul_rslts_post.get(val))

print("input")
print(inp_arr)
print("rslt")
print(rslt)