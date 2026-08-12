numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0:3])

text = "Hello, World!"
print(text[7:12])

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "შავი"]
print(colors[-2:])

short_nums = [1, 2, 3, 4, 90, 8, 72, 31, 74]
total = 0
for num in short_nums:
    total = total + num
print(total)


get_highest = [90, 81, 100, 23, 3, 98, 102, 90, 75]
highest = get_highest[0]  # ← was get_highest[0:4]
for num in get_highest:
    if num > highest:
        highest = num
print(highest) 