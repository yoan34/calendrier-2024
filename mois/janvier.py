import os


sommeil = []
projects = {
    "livre_inaya": [],
    "dessin": [],
    "autre": []
}
disciplines = {
    "maison": [],
    "yogi":   [],
    "sport":  []
}

energie_corps  = []
energie_mental = []
energie_esprit = []

# for i in range(2,32):
#     print(f"DATE: {i:0>2}/01/2024\n")
#     user_sommeil = input("Sommeil: ")
#     user_livre_inaya = input("Livre inaya: ")
#     user_dessin = input("Dessin: ")
#     user_autre_project = input("Autre projet: ")
#     user_maison = input("Maison: ")
#     user_yogi = input("Yogi: ")
#     user_sport = input("Sport: ")
#     user_corps = input("Energie corps: ")
#     user_mental = input("Energie mental: ")
#     user_esprit = input("Energie esprit: ")
    
    
#     sommeil.append(float(user_sommeil))
#     if user_livre_inaya:
#         projects["livre_inaya"].append(int(user_livre_inaya))
#     if user_dessin:
#         projects["dessin"].append(int(user_dessin))
#     if user_autre_project:
#         projects["autre"].append(int(user_autre_project))
    
#     if user_maison:
#         disciplines["maison"].append(int(user_maison))
#     if user_sport:
#         disciplines["sport"].append(int(user_sport))
#     if user_yogi:
#         disciplines["yogi"].append(int(user_yogi))
    
#     energie_corps.append(float(user_corps))
#     energie_mental.append(float(user_mental))
#     energie_esprit.append(float(user_esprit))
#     os.system("clear")
    
print(f"sommeil: {sommeil}")
print(f"projects: {projects}")
print(f"disciplines: {disciplines}")
print(f"energie_corps: {energie_corps}")
print(f"energie_mental: {energie_mental}")
print(f"energie_esprit: {energie_esprit}")


sommeil=  [9.0, 9.0, 9.0, 8.5, 7.0, 9.0, 7.5, 8.5, 6.5, 7.5, 9.5, 9.0, 8.0, 6.5, 9.0, 8.0, 9.0, 8.0, 9.0, 7.25, 7.0, 7.0, 8.75, 6.75, 8.25, 7.5, 8.0, 7.5, 7.0, 7.5]
projects = {'livre_inaya': [90, 270, 180, 30, 30, 180, 60, 30, 120, 120, 210, 210, 240, 210, 150], 'dessin': [2], 'autre': []}
disciplines = {'maison': [30, 60, 240, 60, 60, 30, 90, 30, 60, 30, 30, 30, 30, 45, 30, 30, 240, 30, 90, 30, 30, 30, 30, 60, 30, 30, 150, 30, 30], 'yogi': [30, 30, 30, 45, 30, 30, 30, 45, 15, 30, 15, 30, 60, 15], 'sport': [60, 60, 90, 60, 60, 60, 30, 60, 60, 60, 60, 60, 60, 60, 60]}
energie_corps = [3.0, 5.0, 6.0, 6.0, 6.0, 5.0, 7.0, 7.0, 6.0, 2.0, 4.5, 5.0, 5.0, 4.0, 5.0, 4.0, 6.0, 5.0, 4.0, 6.0, 6.0, 4.0, 6.0, 5.0, 6.0, 4.0, 5.0, 5.0, 5.0, 6.0]
energie_mental = [4.0, 6.0, 6.0, 7.0, 5.0, 5.0, 7.0, 7.0, 5.0, 6.0, 5.0, 6.0, 4.0, 5.0, 5.0, 6.0, 7.0, 5.0, 5.0, 6.0, 6.0, 6.0, 7.0, 7.0, 6.0, 6.0, 4.0, 6.0, 6.0, 6.0]
energie_esprit = [3.0, 6.0, 6.0, 7.0, 6.0, 7.0, 7.0, 7.0, 4.0, 6.0, 7.0, 6.0, 3.0, 5.0, 6.0, 7.0, 7.0, 5.0, 5.0, 6.0, 5.0, 7.0, 7.0, 7.0, 7.0, 6.0, 5.0, 6.0, 6.0, 6.0]

print(f"moy par jour sommeil: {sum(sommeil)/30}")
print(f"moy par jour livre_inaya: {sum(projects['livre_inaya'])/30}")
print(f"moy par jour dessin: {sum(projects['dessin'])/30}\n")
print(f"moy par jour maison: {sum(disciplines['maison'])/30}")
print(f"moy par jour sport: {sum(disciplines['sport'])/30}")
print(f"moy par jour yogi: {sum(disciplines['yogi'])/30}\n")
print(f"moy par jour energie corps: {sum(energie_corps)/30}")
print(f"moy par jour energie mental: {sum(energie_mental)/30}")
print(f"moy par jour energie mental: {sum(energie_esprit)/30}")

print(f"total temps de projets par semaine livre inaya: {sum(projects['livre_inaya'])/60/30*7}")
print(f"total temps de projets par semaine dessin: {sum(projects['dessin'])/60/30*7}")
print(f"total temps de projets par semaine dessin: {sum(projects['autre'])/60/30*7}")
    