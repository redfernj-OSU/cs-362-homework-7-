def fizzbuzz(num):
    if ( (num % 5) == 0 ) and ( (num % 3) == 0 ):
        return "FizzBuzz"

    elif (num % 3) == 0:
        return "Fizz"

    elif (num % 5) == 0:
        return "Buzz"

    else:
        return num

def main():
    for i in range(1, 100):
        print(fizzbuzz(i))

if __name__ == '__main__':
    main()

