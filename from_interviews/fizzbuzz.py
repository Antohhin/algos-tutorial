"""
Задачка с интервью на джуна MLE
# Игра в fizz, bazz
Написать функцию которая выводит от 1 до n, но
- если число делится на 3, выводить fizz
- если на 5, тогда buzz
- если на 3 и на 5 fizzbuzz
"""

def brut_fizzbuzz(
        max_count: int,
        fizz_num: int=3,
        buzz_num: int=5
    ) -> None:
    "print fizz buzz"
    for num in range(1, max_count+1):
        if num % fizz_num == 0 and num % buzz_num == 0:
            print("fizzbuzz")
        elif num % fizz_num == 0:
            print("fizz")
        elif num % buzz_num == 0:
            print("buzz")
        else:
            print(num)

def concat_fizzbuzz(
        max_count: int,
        fizz_num: int=3,
        buzz_num: int=5
    ) -> None:
    "string concat"
    [print('Fizz' * (num % fizz_num == 0) + 'Buzz' * (num % buzz_num == 0)
            or num
            )
              for num in range(1, max_count+1)]
    
if __name__ == '__main__':
    print(
        concat_fizzbuzz(17),
        brut_fizzbuzz(17)
          )