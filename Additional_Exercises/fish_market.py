sk_kilo = float(input())
ca_kilo = float(input())
pa_kilo = float(input())
sa_kilo = float(input())
mi_kilo = int(input())

pal = sk_kilo * 1.60
saf = ca_kilo * 1.80
mi = mi_kilo * 7.50

bill = (pal * pa_kilo) + (saf * sa_kilo) + mi

print(f"{bill:.2f}")
