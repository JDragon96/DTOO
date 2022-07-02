from typing import get_type_hints
import inspect
import json

def IsHaveProperty(target, properties: dict):
    # properties : Dictionary
    flag = False
    for key in properties:
        if key == target: flag = True
    return flag

def GetProperties(target_object):
    properties = {}
    attributes = inspect.getmembers(target_object, lambda a: not (inspect.isroutine(a)))
    result = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]
    for item in result:
        properties[item[0]] = item[1]

    return properties

def Serialization(inputData, rootClass):
    for key in inputData:
        if type(inputData[key]) is list:
            newObject = []
            rootProperties = GetProperties(rootClass)

            for item in inputData[key]:
                if IsHaveProperty(key, rootProperties):
                    newRoot = get_type_hints(rootClass)[key].__args__[0].Create()
                    Serialization(item, newRoot)
                    newObject.append(newRoot)

                else:
                    # DO NOT ACCEPT UNEXPECTED PROPERTY!
                    # rootClass[key] = inputData[key]
                    # rootClass[key].update(key, inputData[key])
                    pass

            rootClass.__dict__[key] = newObject

        elif type(inputData[key]) is not dict:
            rootClass.__dict__[key] = inputData[key]

        else:
            rootClass.__dict__[key] = get_type_hints(rootClass)[key].Create()
            Serialization(inputData[key], rootClass.__dict__[key])

def loadJson(path: str, encoding="UTF-8"):
    with open(path, encoding=encoding) as json_file:
        json_data = json.load(json_file)

    return json_data