n = int(input("请输入小于80的正奇数："))
m = int(input("请输入厚度："))
o = str(input("请输入符号1："))
p = str(input("请输入符号2："))
print(' '*(n//2),str(o),sep='')
for i in range (2,n):
    if i<= ((n+1)//2):
        if i<= m:
            print(' '*((n+1)//2-i),str(o)*(2*i-1),sep='')
        if i>m:
            print(' '*(((n+1)//2-i)),str(o)*m,' '*(2*i-2*m-1),str(o)*m,sep='')
    if i >((n+1)//2):
        print('  ')
print(' '*(n//2),str(o),sep='')
print(' '*(n//2),str(p),sep='')
for i in range (2,n):
    if i<= ((n+1)//2):
        if i<= m:
            print(' '*((n+1)//2-i),str(p)*(2*i-1),sep='')
        if i>m:
            print(' '*(((n+1)//2-i)),str(p)*m,' '*(2*i-2*m-1),str(p)*m,sep='')
    if i >((n+1)//2):
        print('  ')
print(' '*(n//2),str(p),sep='')