travel_log = [
{
  "country": "France",
  "visits": 10,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, no_of_visits, visited_cities):
    travel_log.append({
        "country": country,
        "visits": no_of_visits,
        "cities": visited_cities
    })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)