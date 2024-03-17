def add(num1,num2):
    sum_result = num1 + num2 
    return sum_result

def sub(num1,num2):
    diff_result = num1 - num2 
    return diff_result

def prod(num1,num2):
    prod_result = num1 * num2 
    return prod_result    

def div(num1,num2):
    div_result = num1 / num2 
    return div_result 

def calculate():
    num1 = float(input("Enter the first number: "))

    op = input("Enter sign: ")
    # Input the second number 
    num2 = float(input("Enter the second number: "))
    if op == "+":
        sum = add(num1,num2)
        print(f"The sum of {num1} and {num2} is: {sum}")
    elif op == "-":
        diff = sub(num1,num2)
        print(f"The differnece of {num1} and {num2} is: {diff}")
    elif op =="*":
        multi = prod(num1,num2)
        print(f"The product of {num1} and {num2} is: {multi}")
    elif op =="/":
        quo = div(num1,num2)
        print(f"The quotient of {num1} and {num2} is: {quo}")
    else:
        print("invaild")        

if __name__== "__main__":
    calculate()