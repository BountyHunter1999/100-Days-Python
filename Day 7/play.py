import re

f = "greed"

locations = [i.start() for i in re.finditer("p", f)]

print(locations)

