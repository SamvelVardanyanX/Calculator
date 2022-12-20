import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLUE)

print(input("Добро пожаловать! Вы запустили калькулятор, нажмите ввод: "))

print(Fore.CYAN)

expr = input("Здравствуйте! Ведите математическое выражение: ")
result = numexpr.evaluate(expr)

print(Fore.GREEN)

print(f"Результат: {result}")

input()
