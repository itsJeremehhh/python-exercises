def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    for num in nums:
        if num == 7:
            print("should be true")
        else:
            print("should be false")

    # or 
    # msg = "should be true" if (num == 7) else "should be false"
print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

