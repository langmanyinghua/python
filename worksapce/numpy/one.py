#coding=utf-8
import numpy as np
import pandas

def array():
	array = np.array([0,0.65,7.8,10])
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array
	print array * 2
	print "1 ********************** \n"

	array = np.array([0,6,7,10])
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array
	print array + array
	print "2 ********************** \n"

	array = np.array([0,0.65,7.8,True])
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array
	print "3 ********************** \n"

	array = np.array([0,0.65,7.8,'10',"sdfosd"])
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array
	print "4 ********************** \n"


	array = np.array([[0,0.65,7.8],[0,0.65,7.8]])
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array
	print "5 ********************** \n"

	print "*************** 空数组 ****************"
	print np.zeros_like(10)
	print np.zeros(0)
	print np.zeros((4,5))
	print np.ones(5)
	print np.ones((2,2,3))
	print np.empty((2,3))
	print np.empty((2,3,4))
	print np.empty_like(5)
	print "6 ********************** \n"

	print "*************** 数组版 ****************"
	array = np.arange(10)
	print 'array shape ' + str(array.shape )
	print ' type '+ str(array.dtype)
	print array

def one():
	array = np.arange(10)
	arrsub = array[5:8]
	arrsub1 = array[5:8]
	arrsubcopy = array[5:8].copy()
	print arrsub
	arrsub[0:] = 10
	print arrsub
	print array
	print arrsubcopy
	print arrsub1

def two():
	array = np.array([[1,2,3],[4,5,6],[7,8,9]])
	print array[2,0]



def main():
	two()

if __name__ == '__main__':
	main()