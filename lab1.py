# collections 
# list 

cities = [
    'Tokyo',
    'Dakar',
    'Turkey',
    'buenos Aires',
]

print(cities[2])


# dictionary

california_symbols = {
    "bird": "California quail",
    "animal": "Grizzly bear",
    "flower" : "California poppy",
    "fruit" : "Avocado",
}
print(california_symbols)
print(california_symbols["animal"])

# tuple it same as list but it's an immutable 
stars = (
    "Sol",
    "Alpha Centauri",
    "Barnard",
    "Wolf 395",
)

# exercise 
stars = [
    "Sol",
    "Alpha Centauri",
    "Barnard",
    "Wolf 395",
]
print(stars[3])
peaks = {
    "African" : "Kilimanjaro",
    "Antarctic" : "Vinson",
    "Australian" : "Puncak Jaya",
    "Eurasian" : "Everest",
    "North__American" : "Denali",
    "Pacific" : "Mauna Kea",
    "South_American" : "Aconcagua",
}
print(peaks["Pacific"])


for i in stars :
    print(i)