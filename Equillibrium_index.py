


num_elements = int(input("Enter the number of elements: "))
array = []
for i in range(num_elements):
  element = int(input(f"Enter element {i+1}: "))
  array.append(element)
print("Your entered array is :", array)
if(len(array)==1):
   print("the equillibrium index is :",array[0])
   exit(1)
elif(len(array)==2):
   print("the equillibrium index does not exist")
   exit(1)  
sum_arr = [0] * len(array) 
current_sum=0
for j, num in enumerate(array):
    current_sum = current_sum+num
    sum_arr[j] = current_sum 
print("Your preprocessed array is : ",sum_arr)
Total = sum_arr[-1]
for k in array[1:len(array)-1]:
   Lsum = sum_arr[k]-array[k]
   Rsum = Total - sum_arr[k]
   if(Lsum==Rsum):
    print("The Equillibrium Index is : ",array[k])
else:
      print("NO EQUILLIBRIUM INDEX FOUND")
      
