def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    return factorial(num)

num = int(input("Enter your number: "))
print(f"The Factorial of {num} is {factorial(num)}")