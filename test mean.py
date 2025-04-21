def mean(numbers):
    sum = 0
    for elem in numbers:
        sum += elem
    sum = sum/len(numbers)
    return sum

numbers = [1,2,3]
print("mean:",mean(numbers))