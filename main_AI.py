
'''

ABHINAV GUPTA
2015B4A70602P

EXCEPT INITIAL STATE ALL THINGS WORK ONLY FOR SIZE 4 AND GOAL STATE CAN BE 1 OR 2 DFS IS OPTIMIZED BUT BFS IS NOT
INPUT 1 IS FOR INITIAL STATE , 2 AND 3 ARE FOR  BFS AND DFS

GUI CAN BE SEEN AT EACH RUN
I HAVE NOT MADE SEPARATE GUI FOR ANALYSIS PART



FOR fast output for bfs take percentage < 30


 DFS takes about average of 2 sec to run

'''

import math
from Initial_state import *
from GUI2 import gui
from goal_state import *
from Functions import *
import time

# user
size=4
percentage=30
goal_square=1 # no of square in goal state
dicti={}
for i in range(size*size):
    j=size*(size+1)+(i//size)+size*(i%size)
    dicti[i]=[i,j+size,i+size,j]


option=int(input("Please enter integer from 1 to 3"))

if(option==1):
    size=int(input("enter size"))
    percentage=int(input("enter percentage area covered"))
    print("INITIAL STATE")
    arr=initial_state_generator(size,percentage)
    path=[]
    gui(arr,size,path)

if(option==2):
    size=int(input("enter size"))
    percentage=int(input("enter percentage area covered"))
    goal_square=int(input("enter TARGET GOAL"))
    goal=goal_state(goal_square,size,dicti)
    arr=initial_state_generator(size,percentage)
    path=[]
    print("DFS start")
    start = time.clock()
    pat=[]
    pat=create_root.dfs(arr,goal)
    j=len(pat)-1
    while(j>=1):
        for i in range(2*size*(size+1)):
            if(pat[j][i]!=pat[j-1][i]):
                path.append(i+1)
                break
        j=j-1
    print("Action path",path)
    print("time taken",time.clock() - start)
    gui(arr,size,path)
    print("END DFS")

if(option==3):
    size=int(input("enter size"))
    percentage=int(input("enter percentage area covered"))
    goal_square=int(input("enter TARGET GOAL"))
    goal=goal_state(goal_square,size,dicti)
    arr=initial_state_generator(size,percentage)
    path=[]
    print("BFS start")
    start = time.clock()
    pat=[]
    pat=create_root.bfs(arr,goal)
    j=len(pat)-1
    while(j>=1):
        for i in range(2*size*(size+1)):
            if(pat[j][i]!=pat[j-1][i]):
                path.append(i+1)
                break
        j=j-1
    print("Action path",path)
    print("time taken",time.clock() - start)
    gui(arr,size,path)
    print("END BFS")



print("END")
