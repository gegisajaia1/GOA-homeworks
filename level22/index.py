

fruits = ["ვაშლი", "ბანანი", "ატამი"]
fruits.insert(2,'ფორთოხალი')
print(fruits)


cars = ["BMW", "Mercedes", "Audi", "Tesla"]
cars.pop()  
print(cars)

students = ["ანი", "ლუკა", "ნიკო", "ანი", "მარი"]
print(students.count("ანი"))


cities = ["თბილისი", "ქუთაისი", "ბათუმი", "რუსთავი"]
cities.remove('რუსთავი')
print(cities)


nums = [45, 12, 89, 3, 27]
nums.sort()
print(nums)


colors = ["წითელი", "მწვანე", "ლურჯი"]
green_location=colors.index('მწვანე')
print(green_location)


fav1 = input("შეიყვანე პირველი საყვარელი კერძი: ")
fav2 = input("შეიყვანე მეორე საყვარელი კერძი: ")
fav3 = input("შეიყვანე მესამე საყვარელი კერძი: ")
dishes = [fav1, fav2, fav3]
dishes.sort()
print(dishes)


languages = ["Python", "JS", "C++", "Java"]
languages.pop(0)
print(languages)

inventory = ["laptop", "mouse", "keyboard", "mouse"]
if inventory.count("mouse") > 1:
 inventory.remove("mouse")
print(inventory)


names = ["ნიკა", "ელენე", "გიორგი"]
new_name=input("შეიყვანეთ სახელი: ")
if names.count(input("შეიყვანეთ სახელი: ")) > 0:
    print("ეს სახელი უკვე გვაქვს")
else:
   names.append(new_name)