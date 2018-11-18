#working with while loop
import random
rand_num = random.randrange(1,51)
i = 1
while(i != rand_num):
    i += 1
print("Random Value is:", rand_num)

#working with Break and Continue
j = 1

while j< 20:
    if (i%2 ==0):
        j += 1
        continue
    if j == 15:
        break
    print("odd:",j)

    j += 1