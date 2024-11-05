a = [1, 2, 3]
b = a  # b wskazuje na ten sam obiekt, co a

b.append(4)
print(a)  # Output: [1, 2, 3, 4] - zmiana w b wpłynęła na a



def modify_list(lst):
    lst.append(10)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 10] - lista została zmodyfikowana w funkc