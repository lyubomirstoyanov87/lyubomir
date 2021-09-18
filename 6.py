numbers=input().split( )
n=int(input())
list_numbers=[]
for i in numbers:
    digits=int(i)
    list_numbers.append(digits)

for j in range (n):
    min_number=min(list_numbers)
    list_numbers.remove(min_number)
print(list_numbers)