def findlcm(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while True:
        if ((greater%n1==0) and (greater%n2==0)):
            lcm = greater
            break
        greater += 1
    return lcm

firstnumber = int(input("Please Enter First Number "))
secondnumber = int(input("Please Enter Second Number "))
print("LCM Of %d & %d Is %d" %(firstnumber, secondnumber, findlcm(firstnumber, secondnumber)))
