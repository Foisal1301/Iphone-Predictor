import pandas as p
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as mlt

data = p.read_csv("iphone_price.csv")
#print(data.head())
mlt.bar(data["version"],data["price"])
#mlt.barh(data["version"],data["price"])
#mlt.plot(data["version"],data["price"])
#mlt.scatter(data["version"],data["price"])
mlt.show()
#model = LinearRegression()
#model.fit(data[["version"]],data[["price"]])
#futureVersion = int(input("Which version do you want?:"))
#print(model.predict([[futureVersion]]))