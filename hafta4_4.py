#This is answer to practice 1 page 37

#Define function Fahrenheit
def fahrenheit(celcius):
    return (9/5) * celcius + 32

#Print the table for celcius and fahrenheit
print(f"{"Celcius":<10} {"Fahrenheit":<10}")
print("-" * 20)

#Count the celcius between 0-100
#Answers should be in 1dp (1 kesinlik basamagi)
for celcius_degeri in range(0, 101, 10): #The last comma describes increase by how much
    fahrenheit_degeri = fahrenheit(celcius_degeri)
    print(f"{celcius_degeri:<10} {fahrenheit_degeri:<9.1f}")


