largest = None
smallest = None
while True:
    num = input('Enter a number')
    if num == 'done':
        break
    try:
        n = int(num)
        if largest < n:
            largest = n
        if smallest == None or smallest > n:
            smallest = n
    except:
        print('Invalid input')
        continue
    #print(fval)


#print('All done')
print('Maximum is',largest)
print('Minimum is',smallest)
