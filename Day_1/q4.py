string=input()
segment_integer=int(input())
l=len(string)
temp = ""
arr=[]
for i in range(0,l,segment_integer):
    temp=string[i:i+segment_integer]
    arr.append(temp)

ans=[]
for i in range(len(arr)):
    string_1=""
    t=arr[i]
    for j in range(segment_integer):
        if t[j] not in string_1:
            string_1+=t[j]
    ans.append(string_1)        
print(ans)            