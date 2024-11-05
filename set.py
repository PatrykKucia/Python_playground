#  Pythonie set to zbiór — struktura danych, która przechowuje unikalne elementy w nieuporządkowanej kolejności. Zbiory w Pythonie działają podobnie jak zbiory w matematyce i mają kilka szczególnych cech oraz funkcji.

# Cechy zbioru set
# Unikalność elementów: Zbiory przechowują tylko unikalne elementy, czyli automatycznie eliminują duplikaty.
# Niemodyfikowalność elementów: Elementy w zbiorze muszą być niemutowalne, co oznacza, że mogą to być liczby, łańcuchy znaków, krotki itp., ale nie mogą to być listy ani inne zbiory.
# Brak uporządkowania: Elementy w zbiorze nie są przechowywane w określonej kolejności i nie mają indeksów, co oznacza, że nie można uzyskać dostępu do elementów za pomocą indeksów.
# Tworzenie set
# Zbiór można utworzyć za pomocą funkcji set(), podając do niej iterowalny obiekt (np. listę, krotkę). Alternatywnie, można też utworzyć zbiór za pomocą pary nawiasów klamrowych {}. Przykłady:

# Tworzenie pustego zbioru za pomocą set()
my_set = set()

# Tworzenie zbioru z elementami
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Tworzenie zbioru z listy
my_set = set([1, 2, 2, 3, 4])  # Duplikaty zostaną usunięte
print(my_set)  # Output: {1, 2, 3, 4}
# Uwaga: {} bez zawartości to nie set, tylko pusty słownik. Pusty zbiór tworzymy za pomocą set().

#Operacje na set
#Zbiory obsługują różne operacje matematyczne, takie jak suma, przecięcie, różnica i różnica symetryczna.

#Dodawanie elementów:

my_set.add(6)
print(my_set)  # Dodaje 6 do zbioru

#Usuwanie elementów:

my_set.remove(3)  # Usuwa 3 ze zbioru; błąd, jeśli 3 nie ma w zbiorze
my_set.discard(3) # Usuwa 3, jeśli jest, ale bez błędu, gdy nie ma

#Suma zbiorów (| lub union()):

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

#Przecięcie zbiorów (& lub intersection()):

print(set1 & set2)  # Output: {3}

#Różnica zbiorów (- lub difference()):

print(set1 - set2)  # Output: {1, 2}  # Elementy, które są w set1, ale nie w set2

#Różnica symetryczna (^ lub symmetric_difference()):

print(set1 ^ set2)  # Output: {1, 2, 4, 5}  # Elementy, które są tylko w jednym z tych zbiorów