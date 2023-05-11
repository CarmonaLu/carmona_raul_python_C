print("Cual es tu nombre?")
name = input()
print("Cuál es tu primer apellido?")
lastname = input()
print("Cuál es tu segundo apellido?")
SecondLastname = input()
print("En qué año naciste?")
year = input()
print("En qué mes y día naciste?")
month = input()
day = input ()

name_upper = name.upper(), lastname.upper(), SecondLastname.upper()
name_lower = name.lower(), lastname.lower(), SecondLastname.lower()
actual = int(2022)
int_year = int(year)
edad = actual-int_year
longitud = str(len(name+lastname+SecondLastname))

print("Este es tu nombre completo en mayúsculas")

print(name_upper) 

print("Este es tu nombre completo en minúsculas")

print(name_lower)

print("Esta es tu fecha de nacimiento “dd-mm-aaaa”.")
print(day, month, year)

print("Esta es tu edad")

print(edad)

print("Tu nombre completo tiene " + longitud +" letras.")


print("Tu edad en 10 años será ")

print(edad + 10)
