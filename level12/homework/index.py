number=1
if number>10:
 print("more than 10")
else:
    print("not more than 10")

number1=int(input("enter your number: "))
if number1==15:
    print("equal to 15.")
else:
    print("not equal to 15.")
    
    
string=input("enter your string: ")
if string=="group92":
    print("you are right") 
else:
    print("you are wrong")    
    
    
    
for i in range(50,100,5):
    print(i)
    

    
name="gegi sajaia"

for letter in name:
     print(letter)
     
     
     
number = 20
while number <= 50:
    print(number)
    number += 1
    
for i in range(0, 100):
     print(i)
     
     
     number = 0
while number <= 100:
    print(number)
    number += 1
    
for i in range(101):
      print(i)
    
number = 0
while number <= 100:
    print(number)
    number += 1
    
    
for i in range(10, 20):
        print(i)
        
        

number = 10
while number <= 20:
    print(number)
    number += 1
    
for i in range(100, 200):
    print(i)
    
    
number=100
while number<= 200:
    print(number)
    number+=1        
    
    
for i in range(10, 0):
    print(i)
    
    
    number=10
while number>=0:
        print(number)
        number-=1
        
        
number=int(input("enter your number: "))
if number>0:
 print("ეს რიცხვი დადებითია")

elif number<0:
    print("ეს რიცხვი უარყოფითია: ")
else:
    print("ეს რიცხვი ნულია")    


age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age < 0:
     print("არასწორი ინფო")
elif age <= 12:
     print("ბავშვი ხარ")
elif age <= 19:
     print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
     print("ზრდასრული ხართ")
elif age <= 120:
     print("ხანში შესული ხართ")
else:
     print("გურუ ან ჯადოქარი") 
     
     
number = int(input("enter number: "))
if number > 50:
    print(number * 5)
else:
    print(number ** 2)    
    
password = input("enter password: ")

if password == "goa123":
   print("Password is correct!")
else:
   print("Incorrect password!")    
   
number = int(input("შეიყვანეთ რიცხვი: "))
total = 0
for i in range(1, number + 1):
    total += i
print(total)   


for ticket in range(1, 5001):
    print("ბილეთი")
    if ticket == 2024:
         print("ჯეკპოტი! მომგებიანი ბილეთი ნაპოვნია")
         break
  
  
for i in range(1, 301):
    if i % 4 == 0 and i % 7 == 0:
        print(i)
        break     
    
for i in range(1, 51):
    if i % 10 == 0:
        continue
    print(i)    