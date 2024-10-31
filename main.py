import pandas as pd

data = pd.read_csv("monthly-sold-house-prices.csv")
data.columns = ["ID", "Sold_Price", "Date_Sold", "Postcode", "Type", "Age",
                "Contract", "Building", "Number", "Street",
                "Locality", "Town", "District", "County", "Status", "Change"]

town_is_brighton = data["Town"] == "BRIGHTON"
is_house = (data["Type"] != "F") & (data["Type"] != "O")

# Gets the head of brighton house data and prints average
brighton_house_data = data.loc[town_is_brighton & is_house]
print(brighton_house_data[["Sold_Price", "Building", "Number", "Street", "Type"]].head(3))
brighton_average = brighton_house_data["Sold_Price"].mean()
print(f"Average house price in Brighton: {brighton_average.round()}")

# Apply this logic to every town:
data_light = data[["Sold_Price", "Town", "Type"]]
only_house_data = data_light.loc[is_house]
av_price_in_town = only_house_data.groupby(by="Town", as_index=False)["Sold_Price"].mean().round()
print(av_price_in_town.head(5))

# country average
country_av = data.loc[is_house]["Sold_Price"].mean()
print("\n# country average")
print(country_av.round())

# top 10 percentile
top_10_percentile = av_price_in_town["Sold_Price"].quantile(0.9)
top_towns = av_price_in_town[av_price_in_town["Sold_Price"] >= top_10_percentile]
print("\n# top 10 percentile")
print(top_towns.sort_values(by="Sold_Price", ascending=False).head(10))

# bottom 10 percentile
bottom_10_percentile = av_price_in_town["Sold_Price"].quantile(0.1)
bottom_towns = av_price_in_town[av_price_in_town["Sold_Price"] <= bottom_10_percentile]
print("\n# bottom 10 percentile")
print(bottom_towns.sort_values(by="Sold_Price", ascending=True).head(10))

# most expensive houses. 0.1 percentile
highest_percentile = only_house_data["Sold_Price"].quantile(0.999)
most_expensive_houses = only_house_data.loc[only_house_data["Sold_Price"] >= highest_percentile]
print("\n# Top 0.1 % ")
top_zero_point_one_percent = most_expensive_houses.sort_values(by="Sold_Price", ascending=False)
print(top_zero_point_one_percent.head(10))

print("\n# Top 0.1 % in town aggregate count")
agg = top_zero_point_one_percent.groupby(by="Town", as_index=False)["Sold_Price"].count()
agg.columns = ["Town", "Sold_Count"]
print(agg.sort_values(by="Sold_Count", ascending=False).head())

all_data_only_house = data.loc[is_house]
all_data_minus_ID = all_data_only_house[["Sold_Price", "Postcode", "Building", "Number", "Street"]]
highest_sold_price = all_data_minus_ID["Sold_Price"].max()
highest_price_row = all_data_minus_ID.loc[all_data_minus_ID["Sold_Price"] == highest_sold_price, :]

print("\n# Highest sold price for September")
print(highest_price_row)