a=list(map(int,input().split()))
length=len(a)
count=0
for i in range(length):
    for j in range(i+1,length):
        if a[i]+a[j]==0:
            count+=1
if count>=1:
    print("True")
else:
    print("False")

