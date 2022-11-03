#text cost calculation
text = input()

length = len(text)

cost = length * 60

dollar = cost // 100
cent = cost % 100

print(dollar, "dollars", cent, "cents")