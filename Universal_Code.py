import Data.Language as Language
#region ## Configurações
 


TypeNumber = {int,float}
#endregion
def Fibonacci(limit=1):
        if not type(limit) in TypeNumber :
             return Language.portugues["float_or_int"]
        


        Fibonacci_table=[1,1]
        while True:
            if Fibonacci_table[1] >= limit: 
                return Fibonacci_table[1] 
            else:
                 
                Fibonacci_table[0] = Fibonacci_table[0] + Fibonacci_table[1]
                Fibonacci_table[1] = Fibonacci_table[0] - Fibonacci_table[1]

def Factorial(Number=1):
        if not type(Number) in TypeNumber :
             return Language.portugues["float_or_int"]
        n = Number
        while Number > 1:
              Number=Number-1
              n = n * (Number)
        return n

def IMC(Weight=1,Height=1):
      if not type(Weight) in TypeNumber or not type(Height) in TypeNumber:return Language.portugues["float_or_int"]
      return Weight / (Height*Height)

def Percentage(Number1=0,Number2=0):
        if not type(Number1) in TypeNumber or not type(Number2) in TypeNumber:
             return Language.portugues["float_or_int"]
        return (Number1 / 100) * Number2

def Arithmetic_Average(Numbers=[0,0]):
        if not isinstance(Numbers,list):
              return Language.portugues["list_Error"]
        Final_Number = 0
        for Dados in Numbers:
              
             if not type(Dados) in TypeNumber:
                 return Language.portugues["float_or_int"]
             Final_Number = Final_Number + Dados
        return Final_Number / len(Numbers)

def Geometric_Mean(Numbers=[0,0]):
        if not isinstance(Numbers,list):
              return Language.portugues["list_Error"]
        Number = 1
        for items in Numbers:
             if not type(items) in TypeNumber:
                 return Language.portugues["float_or_int"]
             Number = Number * items
        return pow(Number,1 / len(Numbers))   

