import math
'''

ABHINAV GUPTA
2015B4A70602P

'''

def goal_state(goal_square,size,dicti):
    if(goal_square==1):
        goal=[]
        #size1
        toadd=[0]*40
        for i in range(size*size):
            lis=dicti[i]
            for k in range(len(lis)):
                toadd[lis[k]]=1
            goal.append(toadd)
            toadd=[0]*40
        #size2
        for i in range(size*size):
            if(i%size==size-1):
                continue
            if(i//size==size-1):
                continue
            temp=[0]*4
            temp[0]=i
            temp[1]=i+1
            temp[2]=i+4
            temp[3]=i+5
            sety=set()
            for k in range(len(temp)):
                lis=dicti[temp[k]]
                for t in range(len(lis)):
                    if(lis[t] not in sety):
                        toadd[lis[t]]=1
                        sety.add(lis[t])
                    else:
                        toadd[lis[t]]=0
            goal.append(toadd)
            toadd=[0]*40
        #size4
        toadd=[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
        goal.append(toadd)
        toadd=[0]*40
        #size3
        for i in range(size*size):
            if(i%size>=size-2):
                continue
            if(i//size>=size-2):
                continue
            temp=[0]*9
            temp[0]=i
            temp[1]=i+1
            temp[2]=i+2
            temp[3]=i+4
            temp[4]=i+5
            temp[5]=i+6
            temp[6]=i+8
            temp[7]=i+9
            temp[8]=i+10
            sety=set()
            for k in range(len(temp)):
                lis=dicti[temp[k]]
                for t in range(len(lis)):
                    if(lis[t] not in sety):
                        toadd[lis[t]]=1
                        sety.add(lis[t])
                    else:
                        toadd[lis[t]]=0
            goal.append(toadd)
            toadd=[0]*40
        return goal

    else:
            goal=[]
            temp=[]
            for i in range(15):
                j=i+1
                while j<16:
                    temp.append([i,j])
                    j+=1

            for i in range(len(temp)):
                lissss=temp[i]
                arr=[0]*40
                ml=dicti[lissss[0]]
                for j in range (len(ml)):
                    arr[ml[j]]=1
                ml=dicti[lissss[1]]
                for j in range (len(ml)):
                    arr[ml[j]]=1
                goal.append(arr)
            return goal
