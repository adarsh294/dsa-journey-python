arr=[0,1,2,1,1,3,3]
l=0
mp={}
a=[]
s=set()
for i,j in enumerate(arr):
    s.add(j)
    if j not in mp.values():
        mp[i]=j
        a.append(j)
arr.clear()
arr.extend(a)
print(arr,s)       
