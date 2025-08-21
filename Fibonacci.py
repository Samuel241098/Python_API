def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

user = int(input("Enter the Integer: "))
if user<=0:
    print("Please enter a positive number")
else:
    for i in range(user):
        print(fibonacci(i))
