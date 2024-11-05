# W Pythonie zmienne dzielą się na mutowalne i niemutowalne w zależności od tego, czy ich wartość może być zmieniona po stworzeniu obiektu, do którego są przypisane. 
# Zrozumienie tej różnicy jest ważne, ponieważ wpływa na sposób działania programów i zarządzania pamięcią.

# 1. Zmienne mutowalne
# Zmienne mutowalne to takie, których wartość można modyfikować po ich utworzeniu, bez zmiany odniesienia do obiektu w pamięci. 
# Oznacza to, że można zmieniać ich zawartość (elementy, właściwości) bez konieczności tworzenia nowego obiektu.

# Przykłady typów mutowalnych:
# Listy (list)
# Słowniki (dict)
# Zbiory (set)
# Przykład:

# Tworzymy listę - typ mutowalny
my_list = [1, 2, 3]
print("Przed zmianą:", my_list)  # Output: [1, 2, 3]

# Modyfikujemy zawartość listy
my_list[0] = 10
print("Po zmianie:", my_list)    # Output: [10, 2, 3]
# W powyższym przykładzie modyfikujemy element listy. Python nie tworzy nowej listy, tylko aktualizuje istniejącą. Adres pamięci listy pozostaje ten sam.

# 2. Zmienne niemutowalne
# Zmienne niemutowalne to takie, których wartość nie może być zmieniona po utworzeniu obiektu. 
# Każda próba modyfikacji wartości zmiennej niemutowalnej skutkuje utworzeniem nowego obiektu w pamięci, a zmienna zaczyna odnosić się do nowej wartości.

# Przykłady typów niemutowalnych:
# Liczby całkowite (int)
# Liczby zmiennoprzecinkowe (float)
# Krotki (tuple)
# Łańcuchy znaków (str)
# Typ boolowski (bool)
# Przykład:

# Tworzymy zmienną typu int - typ niemutowalny
a = 5
print("Przed zmianą:", a)  # Output: 5

# Przypisujemy nową wartość
a = a + 1
print("Po zmianie:", a)    # Output: 6
# W tym przypadku zmienna a miała pierwotnie wartość 5, ale przy próbie zmiany na a + 1 (czyli 6) Python tworzy nowy obiekt o wartości 6. Pierwszy obiekt (o wartości 5) pozostaje niezmieniony – zmienia się tylko odniesienie a do nowego obiektu.

# Dlaczego to ważne?
# Rozróżnienie między typami mutowalnymi i niemutowalnymi pomaga zrozumieć, jak Python zarządza pamięcią i jak działają operacje przypisania. 
# Dla typów mutowalnych możliwe jest modyfikowanie zawartości obiektu bez zmiany jego adresu pamięci, co może być bardziej wydajne i oszczędzać pamięć. 
# W przypadku typów niemutowalnych każde przypisanie nowej wartości tworzy nowy obiekt, co zapewnia większe bezpieczeństwo i przewidywalność, ale może być nieco mniej wydajne w niektórych przypadkach.