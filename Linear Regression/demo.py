from numpy import *
data=genfromtxt('C:/Users/balaji.ma/Desktop/testdata.csv', delimiter=',')
x=data[:,0]
y=data[:,1]
print (x)
print (y)
parameters=zeros([2,1])
print (parameters)
#add_1_to_x_matrix

maxX=amax(x)
minX=amin(x)
x = (x - maxX) / (maxX - minX)
print (x)

x=column_stack([ones([len(x),1]),x])
print (x)
parameters=zeros([2,1])
#print (parameters)

print (dot(x,parameters))

#######(x * parameters - y)'  ############
#print (dot(x,parameters)-y)
print (y)
print (y.T)
y=array([y])
#print ('######### (x * parameters - y)' #########' )
print (subtract(dot(x,parameters), y.T))
print ('######### (x * parameters - y) #########' )
print ((subtract(dot(x,parameters), y.T)).T)
print (len(y.T))
print ((  dot ( (subtract(dot(x,parameters), y.T)).T , (subtract(dot(x,parameters), y.T))  ))/(2*len(y.T)) )
