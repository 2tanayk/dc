no_of_nodes = int(input('Enter the no. of nodes: '))
detector_node = int(input('Enter the node no. that detects that the coordinator is down: '))
down_node = int(input('Enter the coordinator node no. that is down: '))
print()

print(f'Node {detector_node} detects that {down_node} is unresponsive/down since it does not respond')
print(f'Hence node {detector_node} starts the election process...')

print()

coordinator = None
lower = []

for i in range(detector_node, no_of_nodes):
    if i == down_node:
        continue
    coordinator = i
    higher = []
    print(f'{i} initiates election procedure')
    for j in range(i + 1, no_of_nodes):
        if j == down_node:
            continue

        print(f'Election message from {i} to {j}')
        higher.append(j)

    if not len(higher) == 0:
        lower.append(i)
        print(",".join(map(str, higher)) + f' all reply with Ok to {i}')
        print(f'hence {i} can\'t be the coordinator')
        print()

print()
print(f'{coordinator} does not get any Ok messages and hence its elected as the coordinator!')
print(f'{coordinator} sends coordinator message to {" ".join(map(str, lower))} ')
