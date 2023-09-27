"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def mean(*numbers: float) -> float:
    """Returns mean average of list of floating point numbers"""
    print(numbers)
    return sum(numbers) / len(numbers)

def median_odd(numList:list) -> float:
    """Called by median() to calculate median from an odd sized list"""
    midpointIndex = len(numList) // 2
    print("Odd", numList[midpointIndex])
    return numList[midpointIndex]

def median_even(numlist:list) -> float:
    """Called by median() to calculate median value of an even sized list"""
    midpointIndex = len(numlist) // 2
    print("Even:",numlist[midpointIndex], numlist[midpointIndex+1])
    return mean(numlist[midpointIndex], numlist[midpointIndex+1])

def median(numList:list) -> float:
    """Returns median value from a list of floating point numbers"""
    sortedList = sorted(numList)
    median = median_even(sortedList) if len(sortedList) % 2 == 0 else median_odd(sortedList)
    return median

def main() -> None:
    """Main method"""
    flag = True
    while flag:
        try:
            print("Enter a list of numbers separated by commas: ")
            numbers = [float(value) for value in input().split(",")]
        except ValueError:
            print("Some input could not be converted to a number!")
        else:
            flag = False
    print(numbers)
    print(sorted(numbers))
    print(median(numbers))

if __name__ == "__main__":
    main()