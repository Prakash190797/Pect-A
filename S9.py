#program on float and their precision

i= 0.1 + 0.1 + 0.1 - 0.3
print(i)

i= .111111111111111111111
j= .000000000000001000001

print("Answer: {:.32}".format(i+j))

#order of operations
#unless we use parentheses, / and * will supersede + and -

print("3 + 4 * 5 = {}".format(3 + 4*5))
print("(3 + 4)* 5 = {}".format((3 + 4)*5))