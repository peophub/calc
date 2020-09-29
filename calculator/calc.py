from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.RED)
print("=========================")
print("| calc made by HackLife |")
print("=========================")
print("Выберите действие:")
print("1) + \n2) *        3) - \n4) /")
a = float(input())
print(Style.RESET_ALL)
print(Back.RED)
if a == 1:
	x1 = float(input("Введите первое число: "))
	x2 = float(input("Введите второе число: "))
	print(x1 + x2)
elif a == 2:
	x1 = float(input("Введите первое число: "))
	x2 = float(input("Введите второе число: "))
	print(x1 * x2)
elif a == 3:
	x1 = float(input("Введите первое число: "))
	x2 = float(input("Введите второе число: "))
	print(x1 - x2)
elif a == 4:
	x1 = float(input("Введите первое число: "))
	x2 = float(input("Введите второе число: "))
	print(x1 / x2)
else:
	print(Style.RESET_ALL)
	print(Fore.RED)
	print("Выбрано неверное действие!")