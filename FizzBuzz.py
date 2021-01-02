def prime(n):
    if n > 1:
        for i in range (2,n):
            if (n % i)  == 0:
                break
        else:
            print("Prime Number")

for num in range (1,101):
    result = ""
    if prime(num):
        result += "Prime"
    else:
        if num % 3 == 0 and num % 5 == 0:
            result += "FizzBuzz"
            print (result)
        elif num % 3 == 0:
            result += "Fizz"
            print(result)
        elif num % 5 == 0:
            result += "Buzz"
            print (result)
        else:
            print(num)
