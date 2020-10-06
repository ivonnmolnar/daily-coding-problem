"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""

def is_sum_in_list(list, k):
    for n in list:
        complement = k-n #value we're looking for that complements n so that n+m=k
        for m in list:
            if(m == complement):
                return True

    return False

test_list = [2,6,1,935,5]
print(is_sum_in_list(test_list,1))
print(is_sum_in_list(test_list,11))
