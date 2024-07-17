#read the number of elements in the array 
num_elements=int(input("Enter the number of elements in the array :"))
array = []
#read the elements of the array
for i in range(num_elements):
    element=int(input(f"Enter the element number {i+1}: "))
    array.append(element)
print("your entered array is : ",array)
#read the number of shifts into a variable called shifts_num
shifts_num = int(input("Enter the number of places by which you have to shift left the elements : "))
#create a loop to iterate number of shift times 
for i in range(0,shifts_num):
    temp=array[0]     #save first element of the array to temp
    #initialise a loop to iterate through the first element to the second last element of the array
    for j in range(0,len(array)-1):
        array[j]=array[j+1]   # one element is replaced by the one immediate after it
    array[len(array)-1]=temp  #this statement is outside the loop and this is to temp as the last element
print("the shifted array is: ",array)