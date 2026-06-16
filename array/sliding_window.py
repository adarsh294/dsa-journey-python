arr=[2,1,5,1,3,2]
k=3
a=0
maxi=0
for i,j in enumerate(arr):
    l=sum(arr[a+i:k+i])
    maxi=max(maxi,l)
print(maxi)
