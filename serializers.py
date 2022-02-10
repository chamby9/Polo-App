import json
def object_to_json(object):

    objectDict = object.__dict__
    jsonString = json.dumps(objectDict)
    print(type(objectDict))
    print(type(jsonString))
    return jsonString
