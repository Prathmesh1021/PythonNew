car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":

print(x)