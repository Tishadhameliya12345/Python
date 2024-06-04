'''

# read CSV file 
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

'''

# file create and read in pandas

import pandas
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)

print()
print("Pandas Series")
# pandas series

import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Lables
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

# Key/Value Objects as Series
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# DataFrames
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

# Read JSON Data
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

# access top records use head()
# access last records use tail()

import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))
print(df.tail(5))
print(df.info())

# use dropna() function
import pandas as pd
df = pd.read_csv('data.csv')
new = df.dropna()
print(df.to_string())
