print("Potapchuk task 21: ")
print("Input the password in the field. It should include at leasl one number, \nat lest one uppercase letter, and at least one lowercase letter.")
password = str(input("Enter String: "))
numbers = [c for c in password if c.isnumeric()]
uppers = [c for c in password if c.isupper()]
lowers = [c for c in password if c.islower()]
for c in password.strip():
if len(password) > 7:
elif c.isnumeric():
elif c.islower():
elif c.isupper():
else:
    return "Strong password"
return "Invalid password"
