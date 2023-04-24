# Round Robin Load Balancing Algorithm
numNodes = int(input("Enter Number of Nodes: "))
numProcesses = int(input("Enter Number of processes: "))

def roundRobin(numNodes, numProcesses):
    ppn = {}
    for i in range(numNodes):
        ppn[i] = 0
    for i in range(numProcesses): 
        # print(i+1)
        a = (i)%numNodes
        curr = ppn[a]
        ppn[a] = curr+1
    print()
    print(ppn)
m=1
while m > 0:
    roundRobin(numNodes,numProcesses)
    print()
    print("Press 1 to add a process\nPress 2 to remove a process\nPress 3 to add a Node\nPress 4 to remove a Node\nPress 5 to exit")
    m = int(input())
    if m==1:
       numProcesses+=1
    elif m==2:
        numProcesses-=1
    elif m==3:
        numNodes+=1
    elif m ==4:
        numNodes-=1
    elif m==5:
        break
    else:
        print('Invalid Input')
        break
