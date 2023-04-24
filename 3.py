#Gloabl Averaging Method

from datetime import timedelta

agreedTime= input("Enter Agreed upon time: ")
numMachines= input("Enter Number of Machines: ")
machineTimes = input(f"Enter current time of {numMachines} Machines: ").split()

def timeToSeconds(time):
    h,m = time.split(":")
    inSeconds = int(h)*60*60 + int(m)*60
    return inSeconds

agreedTimeSeconds = timeToSeconds(agreedTime)
machineTimesSeconds = []
newSkew = []
skew = []

for i in machineTimes:
    machineTimesSeconds.append(timeToSeconds(i))
    
for i in machineTimesSeconds:
    skewTime = i - agreedTimeSeconds
    skewInMin = int(skewTime/60)
    skew.append(skewInMin)

for i in machineTimesSeconds:
    skewTime = i+300 - agreedTimeSeconds
    skewInMin = (skewTime/60)
    newSkew.append(skewInMin)

print(f"Original Skew: {skew}")
print(f"New Skew: {newSkew}\n")

for i in range(len(skew)):
    avg = (skew[i] + newSkew[i])/len(skew)
    if(avg>0):
        print(f"Machine {i} is ahead by {avg}")
        newTime = machineTimesSeconds[i]+300 - avg*60
        print(f"New machine time is {timedelta(seconds=newTime)}\n")
    elif(avg<0):
        print(f"Machine {i} is behind by {avg}")
        newTime = machineTimesSeconds[i]+300 - avg*60
        print(f"New machine time is {timedelta(seconds=newTime)}\n")
