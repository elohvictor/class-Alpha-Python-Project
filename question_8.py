total = 0
for k in range(1, 101):
    if((k%3 == 0) or (k%5 == 0)):
        total +=k
        print("Sum of numbers from 1 to 100 is:", total)