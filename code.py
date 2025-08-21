# pyright: ignore[reportShadowedImports]
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

# Storing operations in a dictionary
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_accumulate=True
    num1=float(input('What is the first number: '))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
            
        operation_symbol=input('Pick and operation: ')
        num2=float(input('What is the next number: '))

        answer=operations[operation_symbol](num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        choice=input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation. ")
        if choice=='y':
            num1=answer
        else:
            should_accumulate=False
            print('\n'*2)
            calculator()
            
calculator()