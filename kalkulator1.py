print("KALKULATOR")

x = input("podaj 1 liczbę: ")
y = input("podaj 2 liczbę: ")


mnożenie = int(x) * int(y)
dodawanie = int(x) + int(y)
odejmowanie = int(x) - int(y)
dzielenie = int(x) / int(y)

działania = ["dodawanie,mnożenie,dzielenie,odejmowanie"]

print("Podaj działanie z listy, które chcesz wykonać", działania)

j = input()

if j == "dodawanie":
    print("wynik: ", dodawanie)
elif j == "mnożenie":
    print("wynik: ", mnożenie)
elif j == "dzielenie":
    print("wynik: ", dzielenie)
else :
    print(mnożenie)
print("Dziękuje za skorzystanie z kalkulatora")







