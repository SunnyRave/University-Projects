i = int(input())
numbers = [int(x) for x in input().split()]

while(len(numbers)>1):
    for n in range(len(numbers)-1):
        if numbers[n]==numbers[n+1]:
            numbers[n] = numbers[n] + numbers[n+1]
            numbers.pop(n+1)
            break
    for m in range(len(numbers)-1):
        if numbers[m]==numbers[m+1]:
            break
        elif m == len(numbers) - 2:
            numbers.pop(numbers.index(min(numbers)))
print(numbers[0])
            
        
