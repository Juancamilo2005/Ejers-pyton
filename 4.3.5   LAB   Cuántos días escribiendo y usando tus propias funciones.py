def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    # Lista de días por mes para años no bisiestos y bisiestos
    days_in_months = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
    days_in_months_leap_year = [
        31, 29, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
    
    # Validación de los argumentos
    if month < 1 or month > 12:
        return None
    
    if year < 1:
        return None
    
    # Determinar si el año es bisiesto
    leap = is_year_leap(year)
    
    # Devolver el número de días del mes dado
    if leap:
        return days_in_months_leap_year[month - 1]
    else:
        return days_in_months[month - 1]

# Casos de prueba
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

print("Resultados de las pruebas:")
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    expected_result = test_results[i]
    result = days_in_month(yr, mo)
    
    if result == expected_result:
        print(f"{yr} {mo} -> OK")
    else:
        print(f"{yr} {mo} -> Fallido: Se esperaba {expected_result}, pero se obtuvo {result}")
