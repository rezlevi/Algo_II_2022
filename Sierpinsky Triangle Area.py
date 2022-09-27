def SierpinskiT(a, b):
    if b == 0:
        return a
    else:
        return SierpinskiT(a*0.75,b-1)

print(SierpinskiT(1,25))