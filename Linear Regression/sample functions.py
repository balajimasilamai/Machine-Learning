#sample functions
from numpy import *
data=genfromtxt('C:/Users/balaji.ma/Desktop/testdata.csv', delimiter=',')
x=data[:,0]
y=data[:,1]
print (x)
print (y)
parameters=zeros([2,1])
print (parameters)
#add_1_to_x_matrix
x=column_stack([ones([len(x),1]),x])

print (x)
learningRate = 0.1
repetition = 20
print ('####### calculating x(:, 1) ########### ')

print (x[:, 0])

print ('####### calculating x(:, 2) ########### ')

print (x[:, 1])

print ('#######################################')


print (parameters[0])
print (parameters[1])
print (parameters)
print ('########### dot multplication ###################################')
print (dot(x,parameters))
print ('######## normal multiplication  ###################')
h = (dot(x,parameters)-y).T
print (dot(h , x[:, 0]))
print (learningRate * dot(h , x[:, 0]))
print ((learningRate * dot(h , x[:, 0]))/len(y))
print ('#################################')
print ((h*x[:,0]*learningRate)/len(y))

def cost(x,y,parameters):
    '''  Calculates the cost function '''
    cost=dot(x,parameters)-y
    transpose=cost.T
    final_cost=dot(transpose,cost)/(2*len(y))
    #print (final_cost)
    #print (sum(final_cost))
    #return final_cost
    return sum(final_cost)


#cost(x,y,parameters)

def gradient(x,y,learningRate,parameters,repetition):
    """
    Main algorithm that tries to minimize our cost functions
    """
    #Getting the length of our dataset
    m=len(y)
    #Creating a vector of zeros for storing our cost function history
    cost_history=zeros([repetition,1])
    #Running gradient descent
    for i in range(0,repetition):
        #Calculating the transpose of our hypothesis
        h = (dot(x,parameters)-y).T
        #Updating the parameters simultaneously
        parameters[0] = parameters[0] - sum((learningRate * dot(h , x[:, 0]))/m)
        parameters[1] = parameters[1] - sum((learningRate * dot(h , x[:, 1]))/m)
        print ('########## parameters #######################')
        print ('parameters[0] : ', parameters[0])
        print ('parameters[1] :' ,parameters[1])
        cost_history[i] = cost(x, y, parameters)
        print ('########### costHistory ##############'
               )
        print(parameters ,cost_history)
        return parameters,cost_history

parameters,cost_history=gradient(x,y,learningRate,parameters,repetition)
print (parameters)
print (cost_history)

