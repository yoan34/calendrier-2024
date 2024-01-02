from datetime import datetime, timedelta

def number_to_date(jour_numero):
    debut_annee = datetime(2024, 1, 1)
    date_cible = debut_annee + timedelta(days=jour_numero - 1)
    return date_cible.strftime("%d/%m/%Y")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fact_prime(n):
    i = 2
    facteurs = []
    while i * i <= n:
        while n % i == 0:
            facteurs.append(i)
            n = n // i
        i += 1
    if n > 1:
        facteurs.append(n)
    degré = len(facteurs)
    return degré

def show_date_per_degre_number(degre):
    c = 0
    for i in range(1,366):
        
        r = fact_prime(i)
        if r == degre:
            c += 1
            print(f"{i:<3} {weeks[i%7-1]:<8} {number_to_date(i):<10} degres={r}")
    print(f"jour total de degres {degre} = {c}")
        

not_mandatory_jeun = [3,7,13,19,31,43,61,73,103,109,131,139,151,181,193,199,229,241,271,283,313,349]
weeks = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
week_dict = {'lundi': 0, 'mardi': 0, 'mercredi': 0, 'jeudi': 0, 'vendredi': 0, 'samedi': 0, 'dimanche': 0}
degres_number = {"0":0, "1":0,"2":0,"3":0, "4":0, "5":0, "6":0, "7":0,"8":0}


# show_date_per_degre_number(8)

for i in range(1,367):
    
    r = fact_prime(i)
    degres_number[str(r)] += 1
    print(f"{i:<3} {weeks[i%7-1]:<8} {number_to_date(i):<10} degres={r}")
    
for key in degres_number:
    print(f"degres {key} = {degres_number[key]:<4} {degres_number[key]/365*100:>5.2f}% de l'année")