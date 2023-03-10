programming_dictionary = {
    "one":"this is the first entry in the dictionary",
    "two":"this is the second entry in the dictionary",
    "three":"this is the third entry in the dictionary",
    "four":"this is the fourth entry in the dictionary",
    "five":"this is the fifth entry in the dictionary",
}

print(programming_dictionary["three"])

print(programming_dictionary)

programming_dictionary["sixth"] = "this is the sixth entry in the dictionary"

print(programming_dictionary)   

empty_dictionary = {}

programming_dictionary["sixth"] = "changed"

print(programming_dictionary)

for i in programming_dictionary:
    print(f"{i} = {programming_dictionary[i]}")

##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}


#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log1 = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log2 = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log3 = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log1)
print(travel_log2)
print(travel_log3)