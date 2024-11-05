print("____Arithmetic____")

a = 10
b = 3
print(f"dodawanie: {a + b}")  # dodawanie
print(f"odejmowanie: {a - b}")  # odejmowanie
print(f"mnożenie: {a * b}")  # mnożenie
print(f"dzielenie z wynikiem float: {a / b}")  # dzielenie z wynikiem float
print(f"dzielenie całkowite: {a // b}") # dzielenie całkowite
print(f"reszta z dzielenia: {a % b}")  # reszta z dzielenia
print(f"potęgowanie: {a ** b}") # potęgowanie
print(f"większe: {a > b}")  # większe
print(f"mniejsze: {a < b}")  # mniejsze
print(f"równe: {a == b}") # równe
print(f"różne: {a != b}") # różne
print(f"większe lub równe: {a >= b}") # większe lub równe
print(f"mniejsze lub równe: {a <= b}") # mniejsze lub równe
print(f"koniunkcja: {a and b}") # koniunkcja
print(f"alternatywa: {a or b}")  # alternatywa
print(f"negacja: {not a}")   # negacja
print(f"bitowe AND: {a & b}")   # bitowe AND
print(f"bitowe OR: {a | b}")   # bitowe OR
print(f"bitowe XOR: {a ^ b}")   # bitowe XOR
print(f"bitowe NOT: {~a}")      # bitowe NOT
print(f"przesunięcie bitowe w lewo: {a << b}")  # przesunięcie bitowe w lewo
print(f"przesunięcie bitowe w prawo: {a >> b}")  # przesunięcie bitowe w prawo
print(f"identyczność: {a is b}")  # identyczność
print(f"różność: {a is not b}") # różność
# The following lines are incorrect and will raise errors, so they are commented out
# print(f"przynależność: {a in b}")  # przynależność
# print(f"brak przynależności: {a not in b}") # brak przynależności
# print(f"konkatenacja: {a + b}")   # konkatenacja
# print(f"powielanie: {a * b}")   # powielanie
# print(f"indeksowanie: {a[0]}")    # indeksowanie
# print(f"wycinanie: {a[1:4]}")  # wycinanie
# print(f"długość: {len(a)}")  # długość
# print(f"konkatenacja: {a + ' 3.8'}") # konkatenacja
# print(f"powielanie: {a * 3}")   # powielanie

print("____strings____")
text = "Python"
print(f"upper: {text.upper()}")      # PYTHON
print(f"lower: {text.lower()}")      # python
print(f"indeksowanie: {text[0]}")           # P - indeksowanie
print(f"wycinanie substringu: {text[1:4]}")         # yth - wycinanie substringu
print(f"długość stringa: {len(text)}")         # długość stringa
print(f"konkatenacja: {text + ' 3.8'}")     # Python 3.8
print(f"powielanie: {text * 3}")          # PythonPythonPython
print(f"podział stringa: {text.split('t')}")   # ['Py', 'hon'] - podział stringa

print("____lists____")

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # dodaje element na końcu
fruits.remove("banana")   # usuwa element
print(fruits[0])          # indeksowanie
print(fruits[-1])         # ostatni element
print(fruits[1:3])        # wycinanie
print(len(fruits))        # długość
fruits.insert(1, "lemon") # wstawia element
print(fruits.count("lemon")) # liczba wystąpień
fruits.pop(1)             # usuwa element
fruits.clear()            # czyści listę
print(fruits)             # []
print(fruits.count("apple")) # liczba wystąpień

print("____tuples____")
#tuples
my_tuple = (1, 2, 3)
print(my_tuple[1])  # dostęp do elementu
print(my_tuple[1:3])  # wycinanie
print(len(my_tuple))  # długość
print(my_tuple.index(3))  # indeks elementu
print(my_tuple.count(3))  # liczba wystąpień
#my_tuple[1] = 4  # nie można zmieniać elementów
#my_tuple.append(4)  # nie można dodawać elementów
#my_tuple.remove(3)  # nie można usuwać elementów
#my_tuple.clear()  # nie można czyścić
#my_tuple.pop()  # nie można usuwać elementów
#my_tuple.insert(1, 4)  # nie można wstawiać elementów

print("____dictionary____")

# Tworzenie słownika o nazwie 'person' zawierającego klucz 'name' z wartością "Alice" oraz klucz 'age' z wartością 25
person = {"name": "Alice", "age": 25}

# Wypisanie wartości przypisanej do klucza 'name' (w tym przypadku "Alice")
print(person["name"])      # Wyświetla: Alice

# Aktualizacja wartości klucza 'age' na nową wartość 26
person["age"] = 26         # Zmienia wiek Alice na 26

# Dodanie nowej pary klucz-wartość 'city' z wartością "New York"
person["city"] = "New York"  # Dodaje nowy klucz 'city' z wartością "New York"

# Wyświetlenie całego słownika 'person'
print(person)              # Wyświetla: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Wyświetlenie liczby elementów (par klucz-wartość) w słowniku 'person'
print(len(person))         # Wyświetla: 3 (bo mamy 3 pary klucz-wartość)

# Opcjonalnie: Usunięcie elementu z kluczem 'age' ze słownika (zakomentowane)
# person.pop("age")         # Usuwa klucz 'age' (nieaktywny z powodu zakomentowania)

# Opcjonalnie: Usunięcie wszystkich elementów ze słownika, co spowoduje jego wyczyszczenie (zakomentowane)
# person.clear()            # Czyści słownik (nieaktywny z powodu zakomentowania)

# Ponownie wyświetlenie słownika 'person' (sprawdzamy aktualny stan)
print(person)              # Wyświetla słownik bez zmian, jeśli poprzednie linie są zakomentowane

# Pobranie wartości przypisanej do klucza 'age' za pomocą metody 'get' (jeśli klucz istnieje)
print(person.get("age"))   # Wyświetla: 26

# Pobranie wartości przypisanej do klucza 'name' za pomocą metody 'get'
print(person.get("name"))  # Wyświetla: Alice

# Wyświetlenie wszystkich kluczy w słowniku 'person'
print(person.keys())       # Wyświetla: dict_keys(['name', 'age', 'city'])

# Wyświetlenie wszystkich wartości w słowniku 'person'
print(person.values())     # Wyświetla: dict_values(['Alice', 26, 'New York'])

# Wyświetlenie wszystkich par klucz-wartość w słowniku 'person'
print(person.items())      # Wyświetla: dict_items([('name', 'Alice'), ('age', 26), ('city', 'New York')])

# Usunięcie i zwrócenie ostatniego elementu ze słownika (FIFO dla słowników od Python 3.7+)
print(person.popitem())    # Usuwa i zwraca ostatnią parę klucz-wartość, np. ('city', 'New York')

# Wyświetlenie słownika 'person' po usunięciu ostatniego elementu
print(person)              # Wyświetla słownik po usunięciu ostatniego elementu (czyli bez 'city')


print("____if statments____")

x = 10
if x > 5:
    print("x jest większe od 5")
elif x == 5:
    print("x jest równe 5")
else:
    print("x jest mniejsze od 5")

print("____loops____")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


count = 0
while count < 5:
    print(count)
    count += 1

print("____functions____")

def greet(name):
    return "Hello, " + name

print(greet("Alice"))

#wartości domyślne
def greet(name="Guest"):
    return "Hello, " + name
print(greet())
print(greet("Alice"))

#funkcje z dowolną liczbą argumentów
def add(*test):
    return sum(test)
print(add(1, 2, 3, 4, 5,5,5,5,5,5,5))

#funkcje z dowolną liczbą argumentów kluczowych
def person(**data):
    print(data)
person(name="Alice", age=25, city="New York")

print("____classes____")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, my name is " + self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

alice = Person("Alice", 25)
print(alice.greet())
print(alice.get_age())
alice.set_age(26)
print(alice.get_age())

print("____exceptions____")

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero")

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(e)

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
finally:
    print("To zawsze się wykona")

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
else:
    print("To się 8 jeśli nie ma błędu")
finally:
    print("To zawsze się wykona")

print("____file operations____")

# Zapis do pliku
with open("test.txt", "w") as file:
    file.write("Hello, World!")

# Odczyt z pliku
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# Dodawanie do pliku
with open("test.txt", "a") as file:
    file.write("Hello, Python!")

# Odczyt z pliku
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

print("____modules____")

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.sqrt(16))

from math import sqrt as s
print(s(16))

print("____packages____")

# Importowanie modułu z pakietu
try:
    from mypackage.mymodule import greet
    print(greet("Alice"))
except ModuleNotFoundError:
    print("Module mypackage.mymodule not found. Please ensure the package and module exist.")

# Importowanie całego pakietu
# import mypackage.mymodule
# print(mypackage.mymodule.greet("Alice"))

# # Importowanie całego pakietu z aliasem
# import mypackage.mymodule as mm
# print(mm.greet("Alice"))

# # Importowanie modułu z pakietu z aliasem
# from mypackage.mymodule import greet as g
# print(g("Alice"))

print("____virtual environment____")

# Instalacja pakietu wirtualnego środowiska
# pip install numpy

# Eksportowanie listy zainstalowanych pakietów
# pip freeze > requirements.txt

# Instalacja pakietów z listy
# pip install -r requirements.txt

print("____tests____")

# Testowanie funkcji greet
assert greet("Alice") == "Hello, Alice"
assert greet("Bob") == "Hello, Bob"

# Testowanie funkcji add
assert add(1, 2, 3, 4, 5) == 15
assert add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55

# Testowanie funkcji person
#assert person(name="Alice", age=25, city="New York") == {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Testowanie klasy Person
alice = Person("Alice", 25)
assert alice.greet() == "Hello, my name is Alice"
assert alice.get_age() == 25
alice.set_age(26)
assert alice.get_age() == 26

print("____end____")

# Zakończenie programu
exit()


