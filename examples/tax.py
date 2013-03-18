def tax(x):
    return x * .05

for x in [100, 200, 300]:
    print(str(x) + " @ 5%: " + str(tax(x)))
