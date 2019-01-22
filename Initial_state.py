'''

ABHINAV GUPTA
2015B4A70602P

'''
import math
import random
import turtle
sqcovered=0
size=0
dicti={}
arr=[]
set1 = set()
def checkpossible(cell,n):
        global arr
        global size
        global dicti
        global set1
        cellr=cell//size+1
        cellc=cell%size+1
        for i in range(1,(n*n)+1):

            temp=[0]*(n*n)
            r=((i-1)//n)+1
            c=(i-1)%n+1

            if(r-1>cellr):
                continue
            if((n-r)>(size-cellr)):
                continue
            if((c-1)>cellc):
                continue
            if((n-c)>(size-cellc)):
                continue

            #generate
            #print("abhi",i)
            temp[c-1]=cell
            p=1;
            while(p<=c-1):
                temp[c-1-p]=cell-p
                p=p+1
            p=1
            while(p<=n-c):
                temp[c-1+p]=cell+p
                p=p+1

            co=1
            p=1
            while(p<=r-1):
                for lom in range(n):
                    temp[co*n+lom]=temp[lom]-size*p
                p=p+1
                co=co+1

            p=1
            while(p<=n-r):
                for lom in range(n):
                    temp[co*n+lom]=temp[lom]+size*p
                p=p+1
                co=co+1


                #print("ab")

            count=0
            flag=1;
            for k in range(len(temp)):

                if(temp[k] in set1):
                    break
                count=count+1
                if(count is n*n):
                    flag=-1
                    break


            if(flag==-1):
                sety=set()
                count=0
                for k in range(len(temp)):
                    if(temp[k]>=0):
                        LIT=dicti[temp[k]]
                        for t in range(len(LIT)):
                            if(LIT[t] not in sety):
                                arr[LIT[t]]=1
                                sety.add(LIT[t])
                            else:
                                arr[LIT[t]]=0
                        set1.add(temp[k])
                        count=count+1

                global sqcovered
                sqcovered=sqcovered+count
                return i

        return -1
    # end function


def initial_state_generator(siz,per):
    global size
    global dicti
    global arr
    global set1
    global sqcovered
    size=siz
    percentage=per
    total_area=size*size
    to_cover_area=(int)((size*size)*percentage)//100
    maxlength=(int)(math.sqrt(to_cover_area))
    arr=[0]*((size+1)*(2*size))
    sqcovered=0
    for i in range(size*size):
        j=size*(size+1)+(i//size)+size*(i%size)
        dicti[i]=[i,j+size,i+size,j]
    count=0;
    while(True):
        ran_no=random.randint(0,size*size-1)
        #print(ran_no)
        if(ran_no in set1):
            continue

        ran_no2=random.randint(1,maxlength)

        pos=checkpossible(ran_no,ran_no2)

        if(pos!=-1):
            #print(ran_no2,pos)
            #print("sq",sqcovered)

            maxlength=(int)(math.sqrt(to_cover_area-sqcovered))
            if(sqcovered==to_cover_area):
                break;
            # end of if

        else:
            continue

        count=count+1
        if(count>=100):
            break
    # end while
    print("Initial filled square",set1)
    print("Initial state",arr)

    return arr
