import math

import math

def sumConstraint(mat):
    change=-1
    temp=[0]*(len(mat)*2+2)
    for(int i=0;i<len(mat);i++):
        sum=0
        flag=0
        for(int j=0;j<len(mat[0]);j++):
            if(mat[i][j]==0):
               flag=1
            sum+=mat[i][j]
        if(change is -1 and flag is 0):
            change=sum
        if(flag is 1 and (sum>change and change is not -1):
            return False
        if(sum!=change and flag is 0):
            return False

    return True



def DFS_BT(matrix,i,j,Blist):




sumConstraint(m)
