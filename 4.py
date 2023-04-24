# Berkley Algorithm
from datetime import timedelta

numClients = int(input("Enter number of clients:"))
clientTimes = input("Enter Client times in HH:MM (24 hr format) separated by a space:").split()
serverTime = input("Enter Server Time in HH:MM (24 hr format):")


def timeToMins(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


serverMins = timeToMins(serverTime)

diff = 0

# calculating the difference from the server
for time in clientTimes:
    diff += (timeToMins(time) - serverMins)

# storing sign of the difference
sign = 1
if diff < 0:
    sign = -1

# abs value for calculation
diff = abs(diff)

adjust = diff / (numClients + 1)
print(adjust)

# hours that need to be added (can be -ve)
adjustHour = adjust // 60

# mins that need to be added (can be -ve)
adjustMins = adjust % 60

# adding the calculated adjustments
serverH = int(serverTime.split(":")[0]) + sign * adjustHour
serverM = int(serverTime.split(":")[1]) + sign * adjustMins

# result
print(f'Synchronized time is {str(int(serverH)).zfill(2)}:{str(int(serverM)).zfill(2)}')
