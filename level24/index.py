def greet(name="World"):
    print(f"Hello {name}")

    
def double(number):
    return number ** 2    
result = double(5)
print(result)

def checkOdd(number):
    if number % 2 == 0:
        return("ლუწი")
    else:
        return("კენტი")
result = checkOdd(7)
print(result)

def BMI(height, weight):
    return weight / (height * height)
result = BMI(1.81, 75)
print(result, 2)