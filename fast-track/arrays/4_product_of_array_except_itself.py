"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Solution:
1. First calculate a prod array that stores product of everything that is left to the current element/
    e.g. for [1, 2, 3, 4], output will be [1, 1, 2, 6]  
    ==> For first element "1", everything to the left is 1
    ==> For second element "2", everything to the left is 1*1=1
    ==> For third element "3", everything to the left is 1*1*2=2
    ==> For fourth element "4", everything to the left is 1*1*2*3=6

2. Similarly, loop from the end and find the product of everything to the right of the current element (starting with 1)
    e.g. for [1, 2, 3, 4], output will be [24, 12, 4, 1]

3. Multiply both the output arrays element-wise to get the final output: [24, 12 , 8, 6]    
"""


def product_array(nums):
    # Naive version: Mine
    prod = 1
    has_zero = False
    for num in nums:
        if num != 0:
            prod *= num
        else:
            has_zero = True
    new_array = []
    for num in nums:
        if has_zero:
            if num == 0:
                new_array.append(prod)
            else:
                new_array.append(0)
        else:
            new_array.append(int(prod / num))

    return new_array


def optimized_product_array(nums):
    prod = 1
    # Store product before that num in the array
    output = []
    for num in nums:
        output.append(prod)
        prod *= num

    print(output)
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * prod
        prod *= nums[i]

    return output


if __name__ == "__main__":
    nums = [-1, 1, 0, -3, 3]
    print(product_array(nums))
    print(optimized_product_array(nums))
