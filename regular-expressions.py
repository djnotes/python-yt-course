import re


list = [
    "The price of rice is $20",
    "The price of meat is $50 per kilo",
    "The price of apples is $10 per kilo",
    "The price of oranges is $10 per kilo"
]


pattern = "^The price of [a-zA-Z]+ is \$([1-9][0-9]*)"


prices = []

for report in list:
    match = re.match(pattern, report) 
    if match is None:
        print("The pattern is not right. Exiting ...")
        exit(1)

    groups = match.groups()
    price = int(groups[0])
    prices.append(price)

print(f"Prices are: {prices}")

sum = 0
for price in prices:
    sum += price

print("Average price is: ", sum/len(prices))

