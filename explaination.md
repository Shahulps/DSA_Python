this is the program to solve the maximum sub array problem with a single loop hence with the least time complexity
what is SUBBARRAYS:it is a collection of elements from one array which appears one afters another in that array
FORMULA : max_sum(i) = max_sum(i-1) + array[i] , array[i])

INCODE FORUMLA : for i in range(1,n):
                      current_sum=max(current_sum+array[i],array[i])
                      max_sum=max(current_sum,max_sum)
