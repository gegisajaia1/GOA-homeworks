# სულ არსებობს 5 შედარებითი ოპერატორი <, >, <=, >= და  ==.
print(5 > 5)
print(5 > 2)
print(5 > 6)
print(5 > 10)

print(5 < 2)
print(3 < 10)
print(2 < 4)
print(1 < 0)
print(242 < 2415)

print(5 >= 5)
print(10 >= 5)
print(10 >= 20)
print(10 >= 10)
print(2941 >= 2)

print(24 <= 25)
print(5 <= 5)
print(2 <= 7285)
print(125 <= 126)
print(214 <= 214)

print(20 == '20')
print(21 == 21)
print(7 == '7')
print(2 == 2)
print(20 == '20')

# logical operator გამოიყენება იმისთვის რომ გავიგოთ მცდარია თუ მართალი მნიშვნელობა   (and და or)
# and ის დროს თუ წინადადებაში სიტყვა false არის მოცემული ტერმინალზე მას გამოიყვანს.
# true ის დროს კი თუ წინადადებაში სიტყვა true არის მოცემული ტერმინალზე მას გამოიყვანს.

print(False and False)
print(False and True)
print(True and False)

print(True or False)
print(False or True)
print(True or True)

number = int(input('enter your number: '))
print(number > 17)

name=input('enter your name: ')
print(name == "gegi")

age=int(input('enter your age: '))
print(age > 18)