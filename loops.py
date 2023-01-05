primes = [2,3,5,7]
for prime in primes:
    print(prime)

print('------------------------------------------')

for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

print('------------------------------------------------')
#while loop
#print out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1

print('-------------------------------')

# break and continue statments

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# print out only odd numbers - 1,3,5,7,9

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('--------------------------------------------------')
count = 0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))


for i in range(1,10):
    if i % 2 == 0:
        break
    print(i)
else:
    print('this cfdghfjghffg')
