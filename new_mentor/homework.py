target = int(input("Enter target: "))

def reachTarget(target):

    # Handling negatives by symmetry
    target = abs(target)

    # Keep moving while sum is smaller of difference is odd
    sum = 0
    step = 0
    while (sum < target or (sum-target) % 2 != 0):
        step = step + 1
        sum = sum + step

    return step

print(reachTarget(target))