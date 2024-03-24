import re

def generator_numbers(text: str):  # пошук сумм в тексті
    yield from re.findall(r"\s\d+\.\d{1,2}\s", text)
def sum_profit(text: str, func: generator_numbers): # обчислення загального доходу після пошуку всіх сум
    numbers = func(text) #  результат пошуку

    total = sum(float(num) for num in numbers)
    return total

def main ():
    text = ("""Загальний дохід працівника складається
    з декількох частин: 1000.01 як основний дохід, 
    доповнений додатковими надходженнями 27.45 і 324.00 доларів"""
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
     main()
