class Operation:
    def __init__(self,nombre1,nombre2):
        self.num1 = nombre1
        self.num2 = nombre2


    def addition(self):
        return self.num1 + self.num2

op = Operation(12,3)



print(op)
print("----------------------")
print("Le nombre1 est",op.num1)
print("----------------------")
print("Le nombre2 est",op.num2)
print("----------------------")
print("Addition",op.addition())