def findgcf(n1, n2):
    if n2!=0:
        return findgcf(n2, n1%n2)
    else:
        return n1

firstnumber = int(input("Please Enter First Number "))
secondnumber = int(input("Please Enter Second Number "))
print("GCF Of %d & %d Is %d" %(firstnumber, secondnumber, findgcf(firstnumber, secondnumber)))
