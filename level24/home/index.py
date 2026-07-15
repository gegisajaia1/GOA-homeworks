# custom ფუნქციებს ერთხელ რომ შევქმნით შეგვიძლია ბევრჯერ გამოვიყენოთ რაც ძალიან მოსახერხებელია. მის შესაქმნელად ვწერთ def-ს ვწერთ სახელს მერე ვწერთ ფრჩხილებს და ბოლოს :-ს. parameter არის ცარიელი ცვლადი. რამდენი parameterიც არის იმდენი argument ია საჭირო

def ჯამი(a, b):
    return a + b
shedegi = ჯამი(10, 15)
print(shedegi) 


def check(num):
    if num % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

check(10)  
check(7)   

def square(num):
    return num ** 2
print(square(10))  

def to_uppercase(text):
    return text.upper()
result = to_uppercase("hello world")
print(result) 

def greet(saxeli, gvari):
    shedegi = "გამარჯობა, მე ვარ " + saxeli + " " + gvari + "."
    print(shedegi)
greet("გეგი", "საჯაია")