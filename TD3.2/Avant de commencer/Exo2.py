def u(n):
    if n==0:
        return 2
    else:
        return (2 * u(n-1)**2 - 1) / (u(n-1)**2 + 2)

#n=0
#while u(n)<30:
#    print(u(n))
#    n=n+1

u=2
n=30
for i in range(n):
    u=(2*u**2-1)/(u**2+2)
    print(u)