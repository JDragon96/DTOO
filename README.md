DTOO: Data To Object in Python
==============================
>  Intro

dtoo is a tool for parsing data to Python Object(class).

> Install
```
>>> pip install dtoo==0.0.2
```

> Example
```
from dtoo import forJson, forModel
from typing import List

####################################
## 1. Input data example
data = {"A": 10,
        "B": 20,
        "C": 30,
        "D": [
                {"Value": 10},
                {"Value": 20}
             ]
        }


####################################
## 2. Class model using for data parsing
## must be decorated by forMdeol.DataClassWrapper
@forModel.DataClassWrapper
class V:
    Value: int = None

@forModel.DataClassWrapper
class Response:
    A: int = None
    B: int = None
    C: int = None
    D: List[V] = None

####################################
## 3. Initialize class instance and run json parsing
res = Response()
dataObject = forJson.Serialization(data, res)
```