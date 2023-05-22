
class stack:
      def __init__(self,inputElement):
        self.inputElement=inputElement
        
        
        
      def push(self,e):

          self.inputElement.append(e)
          
      def reverse(self,r):
          for i in range(len(self.inputElement)):
              r.append(self.inputElement.pop())
          s=''
          for i in r:
              s +=i
          return s
 
 

e=stack([])
e.push('A')
e.push("s")
e.push("m")
e.push("a")
print(e.inputElement)
print(e.reverse([]))





      
    


