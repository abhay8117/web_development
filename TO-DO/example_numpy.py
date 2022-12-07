import  numpy  as  np

arr=np.random.randint((1,50), size=(100,2))
print(arr)

d=[((arr[1][0]-arr[0][0])**2+(arr[1][1]-arr[0][1])**2)**1/2]
d=[(arr[1,0]-arr[0,0])**2+(arr[1,1]-arr[0,1])**2]
print(d)



