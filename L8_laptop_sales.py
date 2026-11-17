import pandas as pd

df = pd.read_csv("laptop sales/Laptop_prices.csv")
print(df.head(11))
print(df.info())
print("the maximum sales of a laptopt where : ",df["Total Sales"].max())
print("the minimum sales of a laptopt where : ",df["Total Sales"].min())
#find the lapotops where the rating is higher than 4.7
above4_7 = df[df["rating"]>4.7]
print(above4_7)
AvailableStockabove400 = df[df["Available Stock"]>400]
print(AvailableStockabove400)
