from _pytest import python

python -m pip install pretty_errors
a = list()
new_list=[1, 2, 3, 4, 5, 6, 7]
a.append(3)
new_list.extend([9,10])
new_list.insert(2, "Edureka!")
print(new_list)
