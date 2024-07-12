num_elements = int(input("Enter the number of elements: "))
array = []
for i in range(num_elements):
  element = int(input(f"Enter element {i+1}: "))
  array.append(element)
print("Your entered list:", array)
def one_loop(array):
    n = len(array)
    max_sum=array[0]
    current_sum=array[0]
    for i in range(1,n):
        current_sum=max(current_sum+array[i],array[i])
        max_sum=max(current_sum,max_sum)
    print("the maximum sum subarray value is:", max_sum)
one_loop(array)