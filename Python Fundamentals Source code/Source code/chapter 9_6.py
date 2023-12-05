# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 08:45:31 2022

@author: msi1
"""

import json
import pandas as pd

x27 = """
{"name": "Adrian",
 "places_lived":["United States", "Canada", "UK"],
 "pet": null,
 "siblings": [{"name":"John", "age":25, "pet":"Bubi"},
              {"name":"Margaret", "age":33, "pet":"Fredo"}
     ]
}
"""

x28 = json.loads(x27)
print ("x28 = \n", x28)
print ("---------------------------")

x29 = json.dumps(x28)
print ("x29 = \n", x29)
print ("---------------------------")

x30 = pd.DataFrame(x28['siblings'], columns=['name', 'age'])

print ("x30 = \n", x30)
print ("---------------------------")
