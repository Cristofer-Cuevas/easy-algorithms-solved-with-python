def oddNumbers(l, r):
    oddNumbers2 = []
    for index in range(l, r+1):
        if index % 2 == 1:
            oddNumbers2.append(index)
    return oddNumbers2
            
print(oddNumbers(3, 9))