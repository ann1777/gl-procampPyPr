print("Potapchuk task 19: ")
print("Input three random numbers - the lengths of the sides of the triangle to check what kind of triangle you can create with sides a, b and c.")
a = int(input("Input a = "))
b = int(input("Input b = "))
c = int(input("Input c = "))
if((a ** 2) < (b ** 2) + (c ** 2)):
    print("It is acute triangular.")
elif((a ** 2) == (b ** 2) + (c ** 2)):
    print("It is rectangular triangular.")
elif((a ** 2) > (b ** 2) + (c ** 2)):
    print("It is obtuse triangular.")
else:
    print("It is impossible to create such triangular.")
