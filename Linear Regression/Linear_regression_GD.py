import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
"""
'''
data=pd.read_csv('C:/Users/balaji.ma/Desktop/testdata.csv',names=['x','y'])

#print (data)
x=np.array(data['x'])
#x.set_index('x', inplace= True)

print (x)
y=np.array(data['y'])
#y.set_index('y', inplace= True)
print (y)

###################################
maxX=max(x)
minX=min(x)

for i in range(0,len(x)):
    #print (x[i]*y[i])
    x_mean = (x[i] - maxX) / (maxX - minX)
    print (x_mean)
    
##############################################
#plt.show()



#print (maxX)
#print (minX)

 
#x = [ones(length(x), 1) x];

#x=np.array[np.zeros(len(x)) ,x]
#print (x)
'''

points = genfromtxt('C:/Users/balaji.ma/Desktop/testdata.csv', delimiter=',')
print (points)
x=points[:,0]
y=points[:,1]
plt.plot(x,'--')
plt.plot(y,'+')
plt.plot(x,y,'ro')
#plt.show()


maxX=max(x)
minX=min(x)

for i in range(0,len(x)):
    #print (x[i]*y[i])
    x_mean = (x[i] - maxX) / (maxX - minX)
    print (x_mean)
print (np.sum(x))

l_ones=np.array(np.ones(len(x)))
x=np.column_stack([l_ones, x])

print (x)

plt.plot(x,y,'go')
plt.show()
mat=np.dot(x,y)
print (mat)
"""
from numpy import *

# minimize the "sum of squared errors". This is how we calculate and correct our error
def compute_error_for_line_given_points(b,m,points):
	totalError = 0 	#sum of square error formula
	for i in range (0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y-(m*x + b)) ** 2
	return totalError/ float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
	#gradient descent
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		print ('####### x is #########')
		print (x)
		print ('##### y is ###########'
                       )
		print (y)
		print ('######  before update b_gradient is ###############')
		print (b_gradient)
		b_gradient += -(2/N) * (y - (m_current * x + b_current))
		print ('######  b_gradient is ###############'
                       )
		print (b_gradient)
		m_gradient += -(2/N) * x * (y - (m_current * x + b_current))
		print ('######  m_gradient is ###############'
                       )
		print (m_gradient)
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	print ('###  new_b and new_m is ########')
	print (new_b, new_m)
	return [new_b,new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):
	b = starting_b
	m = starting_m
	for i in range(num_iteartions):
		b,m = step_gradient(b, m, array(points), learning_rate)
		#print ('b :',b,' m: ',m)
	return [b,m]

def run():
	#Step 1: Collect the data
	points = genfromtxt('C:/Users/balaji.ma/Desktop/testdata.csv', delimiter=',')
	#Step 2: Define our Hyperparameters
	learning_rate = 0.0001 #how fast the data converge
	#y=mx+b (Slope formule)
	initial_b = 0 # initial y-intercept guess
	initial_m = 0 # initial slope guess
	num_iteartions =1
	print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
	print("Running...")
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iteartions)
	print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iteartions, b, m, compute_error_for_line_given_points(b, m, points)))
	return b,m

# main function
if __name__ == "__main__":
	b,m=run()
	print (b,m)
	new_input=8
	op=m+b*new_input
	print ('output= ',op)
