"""
Algorithm Type: Array Traversal
Time Complexity: O(n)
"""
numbers = [4,6,7,1,2,9,3,5,8,0]
target = 22

def two_sum(numbers, target):
    for i in range(len(numbers)):
        if target - numbers[i] in numbers:
            return True
    return False

if __name__ == "__main__":
    print(two_sum(numbers, target))
  
