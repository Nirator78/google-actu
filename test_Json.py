from utils.Json import Json

json = Json('test.json')

print(json.getJson())

json.setJson([{'test': 'test'}])

print(json.getJson())

json.cleanJson()

print(json.getJson())