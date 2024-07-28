import pandas as pd
d={"name":["vivek","Kushi","SK"],
   "roll":[12,13,14],
   "sec":["c1","c3","c2"]
   }
v=pd.DataFrame(d)
p=v.to_csv("Data.csv")
with open("Data.csv","+a") as f:
    f.write("3,adithya,89,c3")

    