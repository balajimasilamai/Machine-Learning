from numpy import *
import matplotlib.pyplot as plt
data=genfromtxt('DataSet.txt', delimiter=',')
x=data[:,0]
y=data[:,1]
print (x)
print (y)
parameters=zeros([2,1])
print (parameters)
#add_1_to_x_matrix


################# feature scaling  #####################################

"""
To make sure features are on a smae scale.
Feature scaling. Feature scaling is a method used to standardize the range of independent variables or features of data.
In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.

More Generally ,Get every feature into approximately  a -1 <= x<=1 range.
eg:
0<=x<=3  good
-2<=x<=0.5   perfect
-100<=x<=100  bad
-0.00001<=x<=0.00001 very bad

Mean Normalization:
 Replace x with x-Ui to make fetaures have zero mean (Do not apply to x0=1)

In this code we have used Mean normalization.
formula:
x=x-Ui/S
where x-- input
Ui--avg value of x in t he training set or (we can use max(x))
S -- Range --> max(x) -min(x) ==> also called standard deviation
"""
maxX=amax(x)
minX=amin(x)
x = (x - maxX) / (maxX - minX)
print (x)
#########################################################################


#################  Learning rate ########################################
"""
How to make sure the gradient descent work correctly?
    --J(theta) ie.cost function should decrease after every iteration.
    --If the J(theta) is increasing after some iteration then we need to reduce the learning rate to converge it.
    

How to choose learning rate?
    --For sufficient amount of learning rate (Aplha),J(theta) should decrease on every iteration.
    --But of Alpha is very small ,Gradient descent can be  slow to converge.
Summary:
    --If Alpha is too small :  Slow convergence
    --If Alpha is too large : J  may not decrease on every iteration;may not converge
    --To choose Alpha try: 0.001,0.003,0.01,0.03,0.1,0.3,1.0,...

"""

learningRate = 0.1



####################################################################
repetition = 2000


x=column_stack([ones([len(x),1]),x])
print (x)
parameters=zeros([2,1])
#print (parameters)
y=array([y])

def cost(x,y,parameters):
    '''  Calculates the cost function '''
    cost=(  dot ( (subtract(dot(x,parameters), y.T)).T , (subtract(dot(x,parameters), y.T))  ))/(2*len(y.T)) 
    #print  (cost)
    return cost
#cost(x,y,parameters)


def gradient(x,y,learningRate,parameters,repetition):
    """
    Main algorithm that tries to minimize our cost functions using Gradient Descent method
    """
    #Getting the length of our dataset
    m=len(y.T)
    #print (m)
    #Creating a vector of zeros for storing our cost function history
    cost_history=zeros([repetition,1])
    #Running gradient descent
    for i in range(0,repetition):
        #Calculating the transpose of our hypothesis
        h = (subtract(dot(x,parameters), y.T)).T
        #print ('#### h value ######')
        #print (h)
        #Updating the parameters simultaneously
        #print ('##### ((learningRate * dot(h , x[:, 0]))/m) ######')
        #print (((learningRate * dot(h , x[:, 0]))/m))
        #print ( parameters[0] - ((learningRate * dot(h , x[:, 0]))/m) )
        parameters[0] = parameters[0] - ((learningRate * dot(h , x[:, 0]))/m)
        parameters[1] = parameters[1] - ((learningRate * dot(h , x[:, 1]))/m)
        #print ('########## parameters #######################')
        #print ('parameters[0] : ', parameters[0])
        #print ('parameters[1] :' ,parameters[1])
        cost_history[i] = cost(x, y, parameters)
        #print ('########### costHistory ##############')
        #print(parameters ,cost_history[i])
    return parameters,cost_history
#gradient(x,y,learningRate,parameters,repetition)
parameters,cost_history=gradient(x,y,learningRate,parameters,repetition)
print (parameters)
#print (cost_history)
plt.plot(data[:,1],'go')
plt.plot(data[:,0],'ro')
#plt.plot(cost_history,'ro')
plt.show()
#prediction

input1=1200
input2 = (input1 - maxX) / (maxX - minX);
output = float(parameters[0]) + (float(parameters[1]) * float(input2))
print ('output is : ',output)
