my_dict = {"Andrey": 1982, "Anton": 1987}
print(my_dict)
print(my_dict["Andrey"])
print(my_dict.get("Sergei"))
my_dict.update({"Kosmos": 2002, "Stas": 2000})
print(my_dict)
a = my_dict.pop("Kosmos")
print(my_dict)
print(a)
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
print(my_set)
my_set.update({6, 7})
print(my_set)
my_set.remove(6)
print(my_set)
