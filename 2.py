multiplier=int(input())
n=int(input())
numbers=[]
for i in range(1,n+1):
    num=i*multiplier
    numbers.append(num)
print(numbers)