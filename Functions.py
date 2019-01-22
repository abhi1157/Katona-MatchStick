import math
import queue
import sys
'''

ABHINAV GUPTA
2015B4A70602P

'''

class create_root():
    def __init__(self,state1,numco,index):
        self.state1=state1
        self.numco=numco
        self.arr=[None]*numco
        self.index=index
        self.curr=0


    def create_node(arr):
        state1=arr
        numco=0
        index=[]

        for i in range(len(state1)):
            if(state1[i]==1):
                numco=numco+1
                index.append(i)
        root=create_root(state1,numco,index)
        return root


    def add_child(node,arr):
        state1=list(arr)
        numco=0
        index=[]

        for i in range(len(state1)):
            if(state1[i]==1):
                numco=numco+1
                index.append(i)
        root=create_root(state1,numco,index)
        if(node.curr<node.numco):
            node.arr[node.curr]=root
            node.curr=node.curr+1


    def next_state(arr,pos):
        state1=list(arr)
        state1[pos]=0
        return state1


    def check_present(goalstate,liss):

        for i in range(len(goalstate)):
            flag=0
            for j in range(40):
                if(goalstate[i][j]!=liss[j]):
                    flag=1
                    break
            if(flag==0):
                print("final state",liss)
                return True

        return False

    def Sort(sub_li):

    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
        sub_li.sort(key = lambda x: x[1])
        return sub_li


    def bfs(instate,goalstate):
            Q = queue.Queue()
            dct={}
            path=[]
            root=create_root.create_node(instate)
            Q.put(root)
            dct[root]=-1
            count=0
            ma=0
            while(Q.qsize()!=0):
                node=Q.get()
                ma=max(ma,Q.qsize())




                if(create_root.check_present(goalstate,node.state1)):
                    #print("what")
                    while(node!=-1):
                        path.append(node.state1)
                        node=dct[node]
                    print("total nodes generated",count)
                    print("maximum stack size",ma)
                    path.append(root.state1)
                    return path

                count=count+node.numco
                for i in range(len(node.index)):
                    nex=create_root.next_state(node.state1,node.index[i])
                    create_root.add_child(node,nex)


                for i in range(node.numco):

                    Q.put(node.arr[i])
                    dct[node.arr[i]]=node

            return path



    def dfs(instate,goalstate):
                St = []
                dct={}
                path=[]
                root=create_root.create_node(instate)
                St.append(root)
                dct[root]=-1
                count=0
                ma=0
                while(len(St)!=0):
                    node=St.pop()
                    ma=max(ma,len(St))
                    count=count+node.numco
                    if(create_root.check_present(goalstate,node.state1)):

                        while(node!=-1):
                            path.append(node.state1)
                            node=dct[node]
                        path.append(root.state1)
                        print("memory for one tree node",sys.getsizeof(root))
                        print("total nodes generated",count)
                        print("maximum stack size",ma)

                        return path

                    lissst=[]
                    for i in range(len(node.index)):
                        l=node.index[i]
                        k=l
                        if(l<=19):
                            k=9*(l//4)+l%4
                        if(l>19):
                            p=4
                            k=(9*(l%4))+p
                            k=k+(l-20)//4
                        lissst.append([l,k])
                    lissst=create_root.Sort(lissst)


                    for i in range(len(lissst)):
                        nex=create_root.next_state(node.state1,lissst[i][0])
                        create_root.add_child(node,nex)
                        St.append(node.arr[i])
                        dct[node.arr[i]]=node



                return path
