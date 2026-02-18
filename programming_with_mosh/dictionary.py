capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Germany": "Berlin"
}
print(dir(capitals))
print(capitals.get("USA"))

capitals.update({"Italy": "Rome", "Spain": "Madrid"})
print(capitals)
capitals.pop("Spain")
print(capitals)
print(len(capitals))

for key in capitals:
    print(f"The capital of {key} is {capitals[key]}")