import math
from scipy.stats import norm

# Hladina významnosti
alpha = 0.05

# Vstupní data pro skupinu B
n1_B = 1822  # Celkový počet smluv v prvním období
m1_B = 513   # Počet smluv s příznakem v prvním období
n2_B = 3358  # Celkový počet smluv ve druhém období
m2_B = 846   # Počet smluv s příznakem ve druhém období

# Výpočet podílů pro obě období
p1_B = m1_B / n1_B
p2_B = m2_B / n2_B

# Výpočet hodnot pro ověření použitelnosti testu
n1p1 = n1_B * p1_B
n2p2 = n2_B * p2_B
n1_1_p1 = n1_B * (1 - p1_B)
n2_1_p2 = n2_B * (1 - p2_B)

# Výpočet kombinovaného podílu
p_combined_B = (m1_B + m2_B) / (n1_B + n2_B)

# Výpočet testového kritéria
U_B = ((p1_B - p2_B) / math.sqrt(p_combined_B * (1 - p_combined_B)) * math.sqrt((n1_B * n2_B) / (n1_B + n2_B)))

# Kritická hodnota
critical_value = norm.ppf(0.95)

# Výstup výsledků
print(f"Podíl smluv s příznakem ve skupině B v prvním období: {p1_B:.4f}")
print(f"Podíl smluv s příznakem ve skupině B ve druhém období: {p2_B:.4f}")
print(f"Kombinovaný podíl pro skupinu B: {p_combined_B:.4f}")
print(f"Testové kritérium: {U_B:.4f}")
print(f"Kritická hodnota pro jednostranný test: {critical_value:.4f}")
print(f"-VYHODNOCENÍ-")

# Ověření použitelnosti testu
if all(value >= 5 for value in [n1p1, n2p2, n1_1_p1, n2_1_p2]):
    print("Test je možné použít.")

    # Rozhodnutí o hypotéze
    if U_B > critical_value:
        print("Zamítáme nulovou hypotézu: Došlo ke statisticky významnému snížení podílu smluv s příznakem.")
    else:
        print("Nezamítáme nulovou hypotézu: Nezjistili jsme statisticky významné sníženípodílu smluv s příznakem.")
else:
    print("Test není možné použít.")