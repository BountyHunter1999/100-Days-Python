# The sum of all the even  numbers from 1 to 100 inclusive

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i

print(f"Sum of all the even numbers is: {sum}")