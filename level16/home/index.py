# slicing python-ში საშუალებას გვაძლევს ამოვჭრათ სიის ნაწილი 
fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)


colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("შეიყვანე ინდექსი 0-დან 4-ამდე: "))
print(colors[index])

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანე ინდექსი 0-დან 3-ამდე: "))
new_color = input("შეიყვანე ახალი ფერი: ")
colors[index] = new_color
print(colors)

numbers_step = [5, 10, 15, 20, 25, 30, 35, 40]
result = numbers_step[::2]
print(result)
 
fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]
result = fruits[2:5]
print(result)

mixed_nums = [12, 45, 8, 33, 91, 24, 10, 77]
for num in mixed_nums:
    if num % 2 == 0:
        print(num)