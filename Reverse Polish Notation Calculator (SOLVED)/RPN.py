# 1 - (2 + 3) * 2
# in RPN:
# 1 2 3 + 2 * -
expr = [1, 2, 3, '+', 2, '*', '-']
def reverse_polish_notation(arr):
      # Fill this in.
      
      #IDEA of RPN:
      # - Stacks data Structure
      # - LIFO --> Last In First Out
      
      #Iterate through array
      # - When you see number, store it into an assigned array
      
      # - When you see an operator, take the last 2 numbers, 
      # and apply that operation on them
      
      
      #Initialize variable to store the number after performing operation on 2 numbers
      current = 0
      
      #Counter for iteration
      count = 0
      
      #Array to store numbers
      newArr = []
      
      #Main Loop
      while count < len(expr):
            
            #If current element is number, store it in newArr
            try:
                  val = int(expr[count])
                  newArr.append(val)        
            
            #If it is not number --> operator
            except ValueError:
                  
                  #When the operator's plus
                  if expr[count]=='+':
                        #Pop out second num in newArr
                        secondNum = newArr.pop()
                        
                        #Pop out first num in newArr
                        firstNum = newArr.pop()
                        
                        #Add them up
                        current = firstNum + secondNum
                        
                        #Store result in newArr
                        newArr.append(current)
                  
                  #The same process for the other 3 operators
                  elif expr[count]=='-':
                        secondNum = newArr.pop()
                        firstNum = newArr.pop()
                        current = firstNum - secondNum
                        newArr.append(current)
                  elif expr[count]=='*':
                        secondNum = newArr.pop()
                        firstNum = newArr.pop()
                        current = firstNum * secondNum
                        newArr.append(current)
                  elif expr[count]=='/':
                        secondNum = newArr.pop()
                        firstNum = newArr.pop()
                        current = firstNum / secondNum
                        newArr.append(current)
            count += 1
      return newArr[0]

print(reverse_polish_notation(expr))
# -9
