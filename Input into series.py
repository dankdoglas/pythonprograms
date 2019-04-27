import pandas as pd

a = input("What is the length of your series, input the value.")
type = input("Do you want a series of Strings or Integers?")

b = []

def intSeries():
    for x in range(0, int(a)):
        c = input("Input the Integers ")
        b.append(int(c))

def stringSeries():
     for x in range(0, int(a)):
        c = input("Input the String ")
        b.append(c)

if "String" in type:
    stringSeries()
    series = pd.Series(b)
    print(series)

else:
    intSeries()
    series = pd.Series(b)
    print(series)
    