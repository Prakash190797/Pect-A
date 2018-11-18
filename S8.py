#working with floats
your_float = input("Enter a float:")
your_float = float(your_float)
print("Rounded to 2 decimals : {:.2f}".format(your_float))

#program on compound interest
money = input("\nHow much to invest:")
int_rate = input("Interest Rate:")

money =  float(money)

int_rate = float(int_rate)*.01
for i in range(10):
    money =  money + (money*int_rate)
print("Investment after 10 years: {:.2f}".format(money))