import numpy as np

"""Numpy arrays allow vectorized operations i.e vector addition,substraction etc
Such additions cannot be done directly using lists

list_two=list(range(1,4))
list_three=list(range(1,4))
list_sum=[]
for i in range(3):
    list_sum.append(list_two[i]+list_three[i])
print(list_sum)"""

#The above operations become very easy when we use Numpy
array_two=np.arange(1,4)
array_three=np.arange(1,4)
print(array_two+array_three)
print(array_two**2)

#Functions in Numpy

print(np.power(np.array([1,2,3,4]),4))
print(np.negative(array_two))
print(np.exp(array_three))
print(np.log(array_three))

#Multidimensional Numpy array objects

"""Defined by shape and whats it composed of
    1D Array: (n,)
    2D Array: (n,m)"""

x=np.arange(0,3)
y=np.arange(3,6)
z=np.arange(6,9)

array_3D=np.array([x,y,z])
print(array_3D)
print(array_3D.shape)

w=np.linspace(1,10,50)  #start,end,samples
w1=np.linspace(1,10,50,False)
print(w1)   #gives evenly spaced samples, last element is excluded
print(w)    #gives evenly spaced samples, last element is included

b=np.arange(1,30,3)
print(b)    #gives every 3rd element from 1 to 30,last element is excluded


#Slicing 1D numpy arrays
print(x[1:3:2]) #start_index,end_index,step

#Reshaping
d=np.arange(18).reshape(3,2,3)
print(d)

#Slicing Multidimensional arrays

print(d[1,:2,:3]) #block,row,coloumn
print(d[:,0,0]) #prints 0,6,12
print(d[1, :2, :3 :2]) #prints 6,8,9,11, block one all rows and columns with step 2

#Comparison
comp=d>5
print(comp) #returns array of true and False
print(d[comp]) #prints elements for which value is True

#Manipulating Array Shapes

k=np.arange(9).reshape(3,3)
ravelled=k.ravel()
print(ravelled) #reshapes k to 1D array

flattened=k.flatten()
print(flattened)    #reshapes k to 1D array

"""Flatten always returns a copy of the array and allocated new memory
whereas ravel returns only view"""

flattened[2]=50
print(k) # No change in original array


ravelled[2]=50
print(k) #we can see 50 in array

"""Ravel is faster than flatten since no memory allocation is involved
But it isnt safe because it changes original array"""


p=np.arange(9)
p.shape=[3,3]
print(p)
print(p.transpose()) # can be done using p.T

#Resizing,unlike reshaping if we give extra dimensions remaining elements are filled with 0
print(np.resize(p,(6,6)))

#Matrix Multiplication

mat_a=np.matrix([0,3,5,5,5,2]).reshape(2,3)
mat_b=np.matrix([3,4,3,-2,4,-2]).reshape(3,2)
print(mat_a*mat_b)
print(np.matmul(mat_a,mat_b))

#Stacking

######Horizontal Stacking###############
a=np.arange(4).reshape(2,2)
b=np.arange(4,8).reshape(2,2)

"""To perform this the arrays must have same shape along 1st axis
It concatenates along the second dimension thereby increasing no of coloumns"""

c=np.hstack((a,b))
print(c)

"""Coloumn Stacking is same as Horizontal stacking in case of multidimensinal
arrays."""

########Vertical Stacking####################
"""To perform this the arrays must have same shape along 2nd axis
It concatenates along the First dimension thereby increasing no of rows"""
print(np.vstack((a,b)))

"""Row Stacking is same as Vertical stacking in case of multidimensinal
arrays."""

"""The same can be achieved by concatenating"""
print(np.concatenate((a,b),axis=1)) # Horizontal
print(np.concatenate((a,b),axis=0)) #Vertical

print(c==np.concatenate((a,b),axis=1))

########Depth Stacking####################

depth_stack=np.dstack((a,b))
print(depth_stack)
print(depth_stack.shape)
