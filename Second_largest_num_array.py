'''this is the optimal solution for finding the second largest number in an array'''
#import sys module to implement max_size and min_size the system can hold
import sys
#next read number of elements in the array and the lements of the array from the user and display it
num_elements = int(input("Enter the number of elements: "))
array = []
for i in range(num_elements):
  element = int(input(f"Enter element {i+1}: "))
  array.append(element)
print("Your entered list:", array)
#my_array.sort() is an inbuild sorting fuction of python which by default sort elements in ascending order. to implement it is descending order
#  Do array.sort(reverse=True) 
array.sort()
print("Your sorted list is: ",array)
#initialise two variables , 'largest' as the first element in the array and 'slargest' as the integer minimum( -sys.maxsize-1)
largest=array[0]
slargest=-sys.maxsize-1
for i in range(len(array)):
#these are the conditions impliesd for optimal calculation
  if(array[i]>largest):
    slargest=largest
    largest=array[i]
  elif(array[i]<largest and array[i]>slargest):
    slargest=array[i]
print("the second largest number in the array is: ",slargest)