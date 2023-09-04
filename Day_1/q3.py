a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    l.append(round(((2*50*a[i])/30)**(1/2)))
print(l)    
