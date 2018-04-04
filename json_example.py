import json

"""
json.load(f): Load JSON data from file (or file-like object)

json.loads(s): Load JSON data from a string

json.dump(j, f): Write JSON object to a file (or file-like object)

json.dumps(j): Output JSON object as string

"""

# json_file = open("./test.json", "r")
# movie = json.load(json_file)
# json_file.close()
# print(movie)
# # Dump string value to json
# print(json.dumps(movie, ensure_ascii=False))
"""
Above code is equivalent to:

with open("test.json") as json_file:
    movie = json.load(json_file)
print(movie)

"""

###############################################################################

value = """{"title": "Tron: Legacy",
     "composer": "Daft Punk",
     "release_year": 2010,
     "budget": 17000000,
     "actors": null,
     "won_oscar": false
     }"""

tron = json.loads(value)
print(tron)
print("tron title and budget are %s and %s respectively" % (tron["title"], tron["budget"]))

to_json_file = open("tron.json", "w")
json.dump(value, to_json_file, ensure_ascii=False)
to_json_file.close()

###############################################################################
