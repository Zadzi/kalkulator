print("KALKULATOR")

first_number = input("podaj 1 liczbę: ")
second_number = input("podaj 2 liczbę: ")


multiplication = float(first_number) * float(second_number)
addition = float(first_number) + float(second_number)
subtraction = int(first_number) - float(second_number)
division = float(first_number) / float(second_number)


actions= ["dodawanie","mnożenie","dzielenie","odejmowanie"]

print("Podaj działanie z listy, które chcesz wykonać", actions)

operation = input()


if operation == actions[0]:
    print("wynik: ", addition)
elif operation == actions[1]:
    print("wynik: ", multiplication)
elif operation == actions[2]:
    print("wynik: ", division)
elif operation == actions[3]:
    print("wynik: ", subtraction)
else:
    print("Nastepnym razem wybierz działanie z listy")

print("Dziękuje za skorzystanie z kalkulatora")







