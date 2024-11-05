# W Pythonie lambda to sposób definiowania funkcji anonimowej, czyli takiej, która nie ma nazwy. 
# Używamy jej głównie do tworzenia małych, jednorazowych funkcji, które nie wymagają pełnej definicji z użyciem słowa kluczowego def. 
# Funkcje lambda są zwłaszcza przydatne, gdy potrzebujemy przekazać funkcję jako argument do innej funkcji lub wykonać prostą operację bez definiowania jej osobno.


# lambda argumenty: wyrażenie
# argumenty — lista parametrów, podobnie jak w zwykłej funkcji.
# wyrażenie — pojedyncze wyrażenie, które zostanie zwrócone jako wynik funkcji lambda.
# Przykład prostej funkcji lambda
# Załóżmy, że chcemy stworzyć funkcję, która zwraca kwadrat danej liczby.

# Funkcja lambda do obliczania kwadratu liczby
kwadrat = lambda x: x ** 2

# Użycie funkcji
print(kwadrat(5))  # Output: 25
#Tutaj lambda x: x ** 2 tworzy funkcję anonimową, która przyjmuje jeden argument x i zwraca jego kwadrat. Po przypisaniu jej do kwadrat, możemy używać jej jak zwykłej funkcji.

# Przykład z wieloma argumentami
# Funkcje lambda mogą przyjmować więcej niż jeden argument. Oto przykład funkcji dodającej dwie liczby:

dodaj = lambda x, y: x + y
print(dodaj(3, 7))  # Output: 10
#Tutaj funkcja lambda przyjmuje dwa argumenty, x i y, i zwraca ich sumę.

# Zastosowania funkcji lambda
# Funkcje lambda są często stosowane z funkcjami wyższego rzędu, takimi jak map(), filter() i sorted(), które wymagają przekazania funkcji jako argumentu.

# Przykład z map()

liczby = [1, 2, 3, 4, 5]
kwadraty = list(map(lambda x: x ** 2, liczby))
print(kwadraty)  # Output: [1, 4, 9, 16, 25]

# Tutaj map() stosuje funkcję lambda lambda x: x ** 2 do każdego elementu listy liczby, zwracając listę kwadratów tych liczb.

# Przykład z filter()

liczby = [1, 2, 3, 4, 5, 6]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)  # Output: [2, 4, 6]
# W tym przykładzie filter() używa funkcji lambda lambda x: x % 2 == 0 do przefiltrowania tylko parzystych liczb z listy liczby.

# Ograniczenia funkcji lambda
# Funkcja lambda może zawierać tylko jedno wyrażenie (nie można używać instrukcji warunkowych, pętli ani innych bloków kodu).
# Zwykle są stosowane do prostych operacji, które nie wymagają pełnej definicji funkcji.
# Funkcje lambda są przydatne do krótkich, jednorazowych zadań, ale w bardziej skomplikowanych przypadkach czytelniejszym wyborem jest pełna definicja funkcji z użyciem def.






