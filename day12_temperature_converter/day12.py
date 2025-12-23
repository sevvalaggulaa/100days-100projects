# Temprature Converter

#Step 1: Define conversion function
def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def parse_values(text):
  parts = text.split(",")
  values = []
  for p in parts:
    p = p.strip()
    if p:
      values.append(float(p))
  return values


#Step 2: Display the menu
def show_menu():
  print("\n--- Temperature Converter Menu (batch supported) ---")
  print("1. Celcius to Fahrenheit & Kelvin")
  print("2. Fahrenheit to Celcius & Kelvin")
  print("3. Kelvin to Celcius & Fahrenheit ")
  print("4. Auto convert")
  print("5. Exit")

#Step 3: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    d

    if choice in ["1","2","3","4"]
      decimal_place = int(input("How many decimal places do you want? (e.g., 2) "))

    if choice == "1":
      text = input("Enter Celcius values separated by commas: ")
      values = parse_values(text)
      for c in values:
        fahrenheit = celcius_to_fahrenheit(c)
        kelvin = celcius_to_kelvin(c)
        print(f"{c}°C = {fahrenheit:.{decimal_place}f}F")
        print(f"{c}°C = {kelvin:.{decimal_place}f}K")


    if choice == "2":
        text = input("Enter Fahrenheit values separated by commas: ")
        values = parse_values(text)
        for f in values:
            celcius = fahrenheit_to_celcius(f)
            kelvin = fahrenheit_to_kelvin(f)
            print(f"{f}F = {celcius:.{decimal_place}f}°C")
            print(f"{f}F = {kelvin:.{decimal_place}f}K")

    if choice == "3":
        text = input("Enter Kelvin values separated by commas: ")
        values = parse_values(text)
        for k in values:
            celcius = kelvin_to_celcius(k)
            fahrenheit = kelvin_to_fahrenheit(k)
            print(f"{k}K = {celcius:.{decimal_place}f}°C")
            print(f"{k}K = {fahrenheit:.{decimal_place}f}F")

    if choice == "4":
        unit = input("What unit are you entering? (C,F,K): ").strip().upper()
        text = input("Enter values separated by commas: ")
        values = parse_values(text)

        for v in values:
          if unit == "C":
            fahrenheit = celcius_to_fahrenheit(v)
            kelvin = celcius_to_kelvin(v)
            print(f"{v}°C = {fahrenheit:.{decimal_place}f}F")
            print(f"{v}°C = {kelvin:.{decimal_place}f}K")

          if unit == "F":
            celcius = fahrenheit_to_celcius(v)
            kelvin = fahrenheit_to_kelvin(v)
            print(f"{v}F = {celcius:.{decimal_place}f}°C")
            print(f"{v}F = {kelvin:.{decimal_place}f}K")

          if unit == "K":
            celcius = kelvin_to_celcius(v)
            fahrenheit = kelvin_to_fahrenheit(v)
            print(f"{v}K = {celcius:.{decimal_place}f}°C")
            print(f"{v}K = {fahrenheit:.{decimal.place}f}K")

          else:
            print("Invalid unit. Please enter C, F, or K")

    if choice == "5":
        print("Exiting the program.")
        break

    else:
      print("Invalid choice. Please select a valid option.")
