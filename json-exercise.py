import json


names = ["Jack", "John", "Mat"]

dictionary = {"name": "Jack", "age": 26, "Profession": "Software Developer"}

name = "John Doe"

age = 30

print("Converting data structures to JSON...")

print(f"{names}. JSON output: {json.dumps(names)}")

print("Dictionary: " )
print(dictionary)
print("Dictionary's JSON format: ") 
print( json.dumps(dictionary))

print("JSON format of " + name + " is ")
print(json.dumps(name))


print("JSON format of age is ")
print( json.dumps(age))

json_str = '''
{
  "browsers": {
    "firefox": {
      "name": "Firefox",
      "pref_url": "about:config",
      "releases": {
        "1": {
          "release_date": "2004-11-09",
          "status": "retired",
          "engine": "Gecko",
          "engine_version": "1.7"
        }
      }
    }
  }
}
'''


print("Decoding some json")

print(f'JSON String: {json_str}')
print(f'Decoded JSON: {json.loads(json_str)}')




dict2 = {"Location": "USA", "Company": "Python"}

encoded = json.dumps(dict2, sort_keys=True)

print(f'Encoded: {encoded}')


