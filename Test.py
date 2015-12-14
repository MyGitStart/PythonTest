l=['mreey','farchk','who','you']
#l.pop(1)
print l
a=l[0]
l[0]=l[-1]
l[-1]=a
a=l[1]
l[1]=l[-2]
l[-2]=a
print l
a=90
if a>60 and a<80:
    print 'ok'
elif a>80:
    print '>80'
else:
    print 'other'
x=1
sum2=0
sum1=0
while x<100:
    if x%2==0:
        sum2+=x
    x=x+1
print sum2
#shi=[1,2,3,4,5,6,7,8,9]
#ge=[0,1,2,3,4,5,6,7,8,9]
#for x in shi:
#    for y in ge:
#        if x<y:
#            print 10*x+y
d={"aa":24,"bb":32,"cc":44,"dd":55}
for m in d:
    print "key:"+m,'value:',d[m]
s=([('a',1),('b',2),('c',3)])
print s
print len(s)
for aa in s:
    print aa
    print aa[0],':',aa[1]
lis=[]
mm=1
while mm<100:
    lis.append(mm*mm)
    mm+=mm
print sum(lis)