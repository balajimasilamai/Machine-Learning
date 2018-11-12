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

learningRate = 0.1
repetition = 200


x=column_stack([ones([len(x),1]),x])
print (x)
parameters=zeros([2,1])
#print (parameters)
y=array([y])

def cost(x,y,parameters):
    '''  Calculates the cost function '''
    cost=(  dot ( (subtract(dot(x,parameters), y.T)).T , (subtract(dot(x,parameters), y.T))  ))/(2*len(y.T)) 
    print  (cost)
    return cost
#cost(x,y,parameters)


def gradient(x,y,learningRate,parameters,repetition):
    """
    Main algorithm that tries to minimize our cost functions
    """
    #Getting the length of our dataset
    m=len(y.T)
    print (m)
    #Creating a vector of zeros for storing our cost function history
    cost_history=zeros([repetition,1])
    #Running gradient descent
    for i in range(0,repetition):
        #Calculating the transpose of our hypothesis
        h = (subtract(dot(x,parameters), y.T)).T
        print ('#### h value ######')
        print (h)
        #Updating the parameters simultaneously
        print ('##### ((learningRate * dot(h , x[:, 0]))/m) ######')
        print (((learningRate * dot(h , x[:, 0]))/m))
        print ( parameters[0] - ((learningRate * dot(h , x[:, 0]))/m) )
        parameters[0] = parameters[0] - ((learningRate * dot(h , x[:, 0]))/m)
        parameters[1] = parameters[1] - ((learningRate * dot(h , x[:, 1]))/m)
        print ('########## parameters #######################')
        print ('parameters[0] : ', parameters[0])
        print ('parameters[1] :' ,parameters[1])
        cost_history[i] = cost(x, y, parameters)
        print ('########### costHistory ##############'
               )
        print(parameters ,cost_history)
        return parameters,cost_history
gradient(x,y,learningRate,parameters,repetition)
