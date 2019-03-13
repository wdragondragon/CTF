str1 = 'gfe-ylcercnsnla-aix{n-pynet-tstmyra}'
g,x,n,c,t,f, = [],[],[],[],[],[]
for i in range(0,35):
    if str1[i]=='g':
        g.append((i+1))
    elif str1[i]=='x':
        x.append((i+1))
    elif str1[i]=='n':
        n.append((i+1))
    elif str1[i]=='c':
        c.append((i+1))
    elif str1[i]=='t':
        t.append((i+1))
    elif str1[i]=='f':
        f.append((i+1))
print('g:'+str(g))
print('x:'+str(x))
print('n:'+str(n))
print('c:'+str(c))
print('t:'+str(t))
print('f:'+str(f))