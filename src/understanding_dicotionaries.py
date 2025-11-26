# Empty Dictionary
homer_0= {
    "color": "yellow", 
    'bag': "maggie-bag", 
    "hair": "black", 
    "dress": "casual", 
    "mom": "false"}
#print (homer_0)
#print(type(homer_0))

marge= {
    "color": "yellow", 
    'bag': "homer-donit", 
    "hair": "blue", 
    "dress": "informal", 
    "mom": "true"}
gun_0 = {"scar": "yellow-orange", "headshot": 1.5}

## Add elements to a dictionary
print(homer_0)
homer_0["x-position"]=15
homer_0["y-position"]=25
homer_0["z-position"]=10
print(homer_0)

marge["x-position"]=16
marge["y-position"]=26
marge["z-position"]=10

alien_0= {"color": "yellow"}
print(alien_0['color'])

# Modifying
alien_0["color"] = "Blue"
print(alien_0)

# Adding elements to a dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["name"]= "Paul"

print(alien_0)

print("\n Looping thought items")
# Items
for key, value in alien_0.items():
    print(f"The key {key}  has value {value}")

#Key
print("\n Loopin tought key")
for key in alien_0.keys():
    print(key)

#Values
print("\n Looping thought values")
for value in alien_0.values():
    print(value)

# NEsting
#List de diccionary
# Listas en diccionarios
# Diccionarios en diccionarios

convenant_grunt = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma-grande",
    "heath": 2
}
convenant_elite = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma-grande",
    "heath": 7
}
convenant_jackal = {
    "color": "gray",
    "weapon": "plasma-gun",
    "armament": "plasma-grande",
    "heath": 5
}

convenants= [
    convenant_grunt,
    convenant_elite,
    convenant_jackal
]
 for convenant in convenants:
    print("\n", convenant)
    for key, value in covenant.items():
        print(key, value)