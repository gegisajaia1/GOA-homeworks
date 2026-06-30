name=input("enter your name")
print(name.lower())

color=input('your fav color: ')
print(color.upper())

city=input('enter your city: ')
print(city.capitalize)

email = "student@university.ge"
print(email.index('@'))

word = "Programming" 
print(word.index('r'))

sentence = "მე მიყვარს ვაშლი და მსხალი."
print(sentence.find('ბანანი'))

info = "Error 404: Page not found"
print(info.find(("404")))

url = "https://www.google.com"
print(url.startswith('https://'))

phone = "+995555123456"
print(phone.startswith('+995'))

filename = "document.pdf"
print(filename.endswith('.pdf'))

sentence=input('enter your sentance: ')
print(sentence.endswith('?'))

word = "abracadabra"
print(word.count("a"))

data = "100110101011"
print(data.count('1'))

products = "პური,რძე,კვერცხი,ყველი"
print(products.split(","))


sentence="hello world"
print(len(sentence))


log_record = ">ERROR: user MARIAM@COMPANY.GE failed to load the backup file. #backup #Server #backup #urgent"


error = log_record.startswith(">ERROR:")
print("არის ეს ერორის ლოგი? -", error)


ends_with_urgent = log_record.endswith("#urgent")
print("მთავრდება #urgent-ით? -", ends_with_urgent)


backup_count = log_record.count("#backup")
print("#backup-ის რაოდენობა:", backup_count)

failed_index = log_record.find("failed")
if failed_index != -1:
    print("'failed'-ის ინდექსი:", failed_index)


at_index = log_record.index("@")
print("'@' სიმბოლოს ინდექსი:", at_index)


words_list = log_record.split(" ")


print("მე-8 სიტყვა დიდი ასოებით:", words_list[7].upper())


email = words_list[2].lower()
print("ელ.ფოსტა:", email)


username = email.split("@")[0]
print("მომხმარებლის სახელი:", username.capitalize())