numbers = [1,2,3,4,5]
list = []
for i in range(len(numbers) -1, -1, -1):
    list.append(numbers[i])
    print("List:", list)