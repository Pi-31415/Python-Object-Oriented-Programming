nums = [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
previous = 0
counter = 0
maximum = 0

for x in nums:
    if(x == 1):
        counter += 1
        if(maximum < counter):
            maximum = counter
    else:
        previous = 0
        counter = 0
    print("x:"+str(x)+" Counter:"+str(counter)+" Maximum:"+str(maximum))
    previous = x
