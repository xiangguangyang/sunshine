x=input('>>>')
x= int(x)
if x%2==0:
    pass
elif x>80:
    pass
else:
    for i in range (-x//2,x+1//2):
        if i <=0:
            print(' '*(-i)+'*'*(x+2*i))
        if i >0:
            print (' '*i+'*'*(x-2*i))
