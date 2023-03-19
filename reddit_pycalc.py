import operator as op

operations = {
    '+': {
        'op': op.add,
        'names': {
            "add",
            "addition",
            "plus",
            "+",
            "combine"
        }
    },
    '-': { 'op':lambda x,y: x-y, 'names': {"subtract", "subtraction", "minus", "-", "deduct", "deduction"}},
    '*': { 'op':lambda x,y: x*y, 'names': {"multiply", "multiplication", "times", "*"}},
    '/': { 'op':lambda x,y: x/y, 'names': {"divide", "division", "obelus", "over", "/", "\\"}}
    }
lookup = { v:operations[k]['op'] for k in operations for v in operations[k]['names'] }

num1 = float(input("Enter first number: "))
operation = input("Enter operation: ").lower()
num2 = float(input("Enter second number: "))

if operation in lookup:
    result = lookup[operation](num1,num2)
    print( int(result) if result.is_integer() else result )
else:
    print("Error: Unknown operation.")

num1 = float(input("Enter first number: "))
operation = input("Enter operation: ").lower()
num2 = float(input("Enter second number: "))

addition = ["add", "addition", "plus", "+", "combine"]
subtraction = ["subtract", "subtraction", "minus", "-", "deduct", "deduction"]
multiplication = ["multiply", "multiplication", "times", "*"]
division = ["divide", "division", "obelus", "over", "/", "\\"]

def calculator(num1, num2, operation):
    if operation in addition:
        return num1+num2
    elif operation in subtraction:
        return num1-num2
    elif operation in multiplication:
        return num1*num2
    elif operation in division:
        return num1/num2
    else:
        return ("Error: Unknown operation.")
        
result = calculator(num1, num2, operation)

#OPTION 1:
try:
    if result.is_integer():
        print(int(result))
    else:
        print(result)
except:
    print(result)


#OPTION 2:
#if isinstance(result, float):
#    if result.is_integer():
#        print(int(result))
#    else:
#        print(result)
#else:
#    print(result)
   
