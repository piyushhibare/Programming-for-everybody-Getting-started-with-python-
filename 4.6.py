def computepay(h,r):
    if h < 40 or r < 0:
        return None
    elif h > 40:
        return (40*r+(h-40)*1.5*r)
    else:
        return (h*r)

try:
    hrs = input("Enter hours")
    hours = float(hrs)
    r = input("Rates ")
    rate = float(r)
    P = computepay(hours,rate)
    print(P)

except:
    print('input your numberic')
