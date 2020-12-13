class Solution:
    def tribonacci(self, n):
        #initialize first 3 elements they need to be known to calculate the next ones
        arr = [0,1,1]
        #start the loop at index 3 
        count = 3 
        #if input asking for 0th element, return 0th element as it's already known
        if n == 0:
            return 0
        #if input asking for 1st element, return 1st element as it's already known
        elif n == 1:
            return 1
        #if input asking for 2nd element, return 2nd element as it's already known
        elif n == 2:
            return 1
        
        #loop for the next elements
        else:
            #while loop end before reaching n+1 due to the indexing in python
            #E.g. if n=9, end loop before n+1(10)-->count<10--->count reaches 9 elements
            #if it was count<n -->count<9 -->reaches 8 elements only
            while count < n+1:
                #create a space in the list for next elements
                arr.append(0)
                #recursive formula F(n) = F(n-1) + F(n-2) + F(n-3)
                arr[count] = arr[count-1] + arr[count-2] + arr[count-3]
                #increment counter
                count+=1
        #arr[count-1] because for n=9, indexing goes 0,1,...,8 -->9 elements
        return arr[count-1]

n = 4
print(Solution().tribonacci(n))
#4

n = 25
print(Solution().tribonacci(n))
#1389537