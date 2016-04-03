import json

def Solve(list,col):
    print(str(list),' ',str(col))
    if col < N:
        for i in range(N):
            if CanPlace(list,col,i):
                list[col] = i
                col+=1
                list,status = Solve(list,col)
                if status:
                    return list,True
                else :
                    col-=1
                    list[col] =-1
        return list,False
    else:
        return list,True
    
def CanPlace(list,col,row):
    #print(str(list),' ' ,str(col),' ' ,str(row))
    for i in range(col):
        if row == list[i]:
            return False
    for i in range(1,col+1):
        if list[col-i] == row-i:
            return False
        if list[col-i] == row+i:
            return False
    return True

json_data = open('input.json')
data =json.load(json_data)
json_data.close()


N=data['N']
no=data['First']

list= [-1]*N

list[0] =no
list,status = Solve(list,1)
if status:
    print('Solved - ',str(list))
else:
    print('Not possible to solve')
