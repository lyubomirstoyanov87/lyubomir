str=input()
nums_str=str.split(', ')

list_numbers=[]
for num in nums_str:
    number=int(num)
    list_numbers.append(number)
print(list_numbers)
index=0
for i in list_numbers:
    list_numbers[index]+=10
    index+=1
print(list_numbers)