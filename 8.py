import numpy as np

numProcesses = int(input("Enter the no. of processes: "))
numResources = int(input("Enter the no. of resources: "))

resourceMap = {}
maxMap = {}
allocMap = {}
needMap = {}
availableMap = {}
sumAlloc = [0]*numResources
totalResources = []
executedOrder = []

for i in range(numResources):
    resourceUnits = int(input(f"Enter the no. of resources for resource type R{i}: "))
    resourceMap[i] = resourceUnits
    totalResources.append(resourceUnits)

print("Enter the Max resources for Process: ")
for i in range(numProcesses):
    processMax = input(f"P{i}: ").split()
    processMax = [int(x) for x in processMax]
    maxMap[i] = processMax

print("Enter the Alloc resources for Process: ")
for i in range(numProcesses):
    processAlloc = input(f"P{i}: ").split()
    processAlloc = [int(x) for x in processAlloc]
    allocMap[i] = processAlloc
    sumAlloc = np.add(np.array(sumAlloc),np.array(processAlloc))

print("Need Matrix: ")
for i in range(numProcesses):
    max = maxMap[i]
    alloc = allocMap[i]
    need = np.subtract(np.array(max),np.array(alloc))
    needMap[i] = need
    print(f"P{i}: {need}")

availableResources = np.subtract(np.array(totalResources),np.array(sumAlloc))
print(f"Resources Remaining: {availableResources}")

for i in range(numProcesses):
    for i in range(numProcesses):
        if(len(needMap.keys()) > 0):
            if(needMap[i].tolist() == [0]*numResources):
                print(f"Process P{i} has executed and resources have been made available")
                availableResources = np.add(availableResources,np.array(allocMap[i]))
                print(f"Available Resources: {availableResources}")
                executedOrder.append(i)
                del needMap[i]
                continue
            if(np.greater_equal(availableResources,np.array(needMap[i])).all()):
                print(f"Process P{i} has executed and resources have been made available")
                availableResources = np.add(availableResources,np.array(allocMap[i]))
                print(f"Available Resources: {availableResources}")
                executedOrder.append(i)
                del needMap[i]
if(len(executedOrder) == numProcesses):
    print("System is in a safe state. The Safe Sequence is: ")
    print(executedOrder)
else:
    print("System is unsafe.")
