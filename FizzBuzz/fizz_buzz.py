def fizz_buzz(int_argument):
    while isinstance(int_argument, int):

        if int_argument%3 == 0 and int_argument%5 == 0:
            return "FizzBuzz"

        elif int_argument%3 == 0:
            return "Fizz"

        elif int_argument%5 == 0:
            return "Buzz"
        else:
            return int_argument

    return None
