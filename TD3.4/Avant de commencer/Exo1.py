def u(n):
    return (2 * n**2 - 1 ) / (n**2 + 2)

#print(u(10))
#print(u(100))
#print(u(1000))

#for n in range(1,10):
    #print(u(n))

n=0
while u(n)<1000:
    print(u(n))
    n=n+1

print(n)
