# Tworzenie frozenset z listy
immutable_set = frozenset([1, 2, 3, 4])

print(immutable_set)  # frozenset({1, 2, 3, 4})

# Próbujemy dodać element - spowoduje błąd
immutable_set.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'