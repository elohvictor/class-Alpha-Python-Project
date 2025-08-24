nums = (1, 2, 3, 4, 5, 6)
even = odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        print(f"Even: {even}, Odd: {odd}")