import math
from scipy.stats import norm

# Hladina významnosti
alpha = 0.05

# Vstupní data pro skupinu A
n1_A = 1928  # Celkový počet smluv v prvním období
m1_A = 289   # Počet smluv s příznakem v prvním období
n2_A = 3661  # Celkový počet smluv ve druhém období
m2_A = 499   # Počet smluv s příznakem ve druhém období

# Výpočet podílů pro obě období
p1_A = m1_A / n1_A
p2_A = m2_A / n2_A

# Výpočet hodnot pro ověření použitelnosti testu
n1p1 = n1_A * p1_A
n2p2 = n2_A * p2_A
n1_1_p1 = n1_A * (1 - p1_A)
n2_1_p2 = n2_A * (1 - p2_A)

# Výpočet kombinovaného podílu
p_combined_A = (m1_A + m2_A) / (n1_A + n2_A)

# Výpočet testového kritéria
U_A = ((p1_A - p2_A) / math.sqrt(p_combined_A * (1 - p_combined_A)) * math.sqrt((n1_A * n2_A) / (n1_A + n2_A)))

# Kritické hodnoty pro oboustranný test
critical_value1 = norm.ppf(alpha / 2)
critical_value2 = norm.ppf(1 - alpha / 2)

# Výstup výsledků
print(f"Podíl smluv s příznakem ve skupině A v prvním období: {p1_A:.4f}")
print(f"Podíl smluv s příznakem ve skupině A ve druhém období: {p2_A:.4f}")
print(f"Kombinovaný podíl pro skupinu A: {p_combined_A:.4f}")
print(f"Testové kritérium: {U_A:.4f}")
print(f"Kritické hodnoty pro oboustranný test: {critical_value1:.4f}, {critical_value2:.4f}")
print(f"-VYHODNOCENÍ-")

# Ověření použitelnosti testu
if all(value >= 5 for value in [n1p1, n2p2, n1_1_p1, n2_1_p2]):
    print("Test je možné použít.")

    # Rozhodnutí o hypotéze
    if U_A < critical_value1 or U_A > critical_value2:
        print("Zamítáme nulovou hypotézu: Došlo ke statisticky významné změně podílu smluv s příznakem.")
    else:
        print("Nezamítáme nulovou hypotézu: Nezjistili jsme statisticky významnou změnu v podílu smluv s příznakem.")
else:
    print("Test není možné použít.")