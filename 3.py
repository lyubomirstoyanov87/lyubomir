Team_A=[1,2,3,4,5,6,7,8,9,10,11]
Team_B=[1,2,3,4,5,6,7,8,9,10,11]
Cards=input()
Cards=Cards.split()

for i in Cards:
    if i[0]=='A':
        index=int(i.split('-')[1])
        if index in Team_A:
            Team_A.remove(index)
    elif i[0]=='B':
        index=int(i.split('-')[1])
        if index in Team_B:
            Team_B.remove(index)
    if len(Team_A)<=7 or len(Team_B) <= 7:
        break
Team_A_count=len(Team_A)
Team_B_count=len(Team_B)
print(f'Team A - {Team_A_count}; Team B - {Team_B_count}')
if Team_A_count <7 or Team_B_count <7:
    print('Game was terminated')
