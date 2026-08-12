# კომენტარებით ახსენით თუ რას აკეთებს .upper(); .lower(); .capitalize(); .find(), .count(), len(), .endswith(), .startswith() ფუნქციები.
# .upper() წერს სიტყვას დიდი ასოებით
# .lower წერს სიტყვას პატარა ასოებით
#.capitalize() იწყებს სიტყვას დიდი ასოთი
#.find() გვეუბნება მერამდენე პოზიციაზეა სიტყვა ან სიმბოლო. თუ იპოვა გამოიტანს რიცხვს და თუ ვერ იპოვა გამოიტანს -1 ს
# .count() ითვლის რამდენჯერ გვხვდება კონკრეტული სიმბოლო ან სიტყვა ტექსტში

sentance=input('enter your sentance: ')
print(sentance.lower())

email = input("enter your email: ")
print(email.find('@'))

book=input('enter book name: ')
print(book.title())

sentance=input('enter your sentance: ')
symbol=input('enter symbol: ')
print(sentance.find(symbol))


word = input('enter word: ')
if word.isupper():
 print("სიტყვა უკვე დიდია!")
else:
 print(word.upper())