def findMedian(firstArrayOfNumbers, secondArrayOfNumbers):
    """
    This function takes two sorted arrays and returns their median.

    Function Parameters:
    firstArrayOfNumbers (List[int]): First sorted array
    secondArrayOfNumbers (List[int]): Second sorted array

    Returns:
    float: Median of the two sorted arrays
    """
    # Validate input types
    if not isinstance(firstArrayOfNumbers, list) or not isinstance(secondArrayOfNumbers, list):
        raise ValueError("Both inputs must be lists.")

    # Validate elements in the lists
    for num in firstArrayOfNumbers + secondArrayOfNumbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the arrays must be integers or floats.")

    # Ensure firstArrayOfNumbers is the smaller array to minimize the binary search space
    if len(firstArrayOfNumbers) > len(secondArrayOfNumbers):
        firstArrayOfNumbers, secondArrayOfNumbers = secondArrayOfNumbers, firstArrayOfNumbers

    # Lengths of the arrays
    lenOfFirstArray, lenOfSecondArray = len(firstArrayOfNumbers), len(secondArrayOfNumbers)

    # Binary search on the smaller array
    minimumNum, maximumNum, half_length = 0, lenOfFirstArray, (lenOfFirstArray + lenOfSecondArray + 1) // 2

    while minimumNum <= maximumNum:
        i = (minimumNum + maximumNum) // 2
        j = half_length - i

        # Binary search adjustments
        if i < lenOfFirstArray and firstArrayOfNumbers[i] < secondArrayOfNumbers[j - 1]:
            minimumNum = i + 1  # i is too small, must increase it
        elif i > 0 and firstArrayOfNumbers[i - 1] > secondArrayOfNumbers[j]:
            maximumNum = i - 1  # i is too big, must decrease it
        else:
            # i is perfect

            # Find max of left part
            if i == 0: max_of_left = secondArrayOfNumbers[j - 1]
            elif j == 0: max_of_left = firstArrayOfNumbers[i - 1]
            else: max_of_left = max(firstArrayOfNumbers[i - 1], secondArrayOfNumbers[j - 1])

            # If it is odd, return max_of_left
            if (lenOfFirstArray + lenOfSecondArray) % 2 == 1:
                return max_of_left

            # Find min of right part
            if i == lenOfFirstArray: min_of_right = secondArrayOfNumbers[j]
            elif j == lenOfSecondArray: min_of_right = firstArrayOfNumbers[i]
            else: min_of_right = min(firstArrayOfNumbers[i], secondArrayOfNumbers[j])

            # If even, return the average of max_of_left and min_of_right
            return (max_of_left + min_of_right) / 2.0


try:
    print(findMedian([1, 3], [2]))  # Output: 2.0
    print(findMedian([1, 2], [3, 4]))  # Output: 2.5
    print(findMedian([1, 7, 9, 4, 5, 33, 45, 78], [3, 4, 6, 8]))  # Output: 4.5
    print(findMedian([1, 3], "not a list"))  # This will raise a ValueError
except ValueError as e:
    print(e)
