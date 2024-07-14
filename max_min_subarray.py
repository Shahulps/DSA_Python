num_elements = int(input("Enter the number of elements: "))
array = []
for i in range(num_elements):
  element = int(input(f"Enter element {i+1}: "))
  array.append(element)
print("Your entered list:", array)
length=int(input("enter the given fixed array length : "))

def trivial(array,length):
  maximum = min(array[:length])
  for i in range(len(array)-length+1):
    minimum=min(array[i:i+length])
    maximum=max(maximum,minimum)
  print("the maximum minimum of the given length subarray is ", maximum)
trivial(array,length)