from art import logo

print(logo)

def primary(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2
    
    
def calculator():
    number1 =float(input("What's the first number? :"))
    print("+\n-\n*\n/")
    
    loop = True
    while loop:  
        operation = input("What's the operation? :")
        number2 = float(input("What's the next number? :"))
        result = primary(number1,number2, operation)
        print(f"{number1}{operation}{number2} = {result}")
        print(result)
        
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()=='y':
            number1 = result
        else:
            loop=False
            calculator()
    
calculator()