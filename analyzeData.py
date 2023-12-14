import pandas as pd
import matplotlib.pyplot as plt

def createTable(file_path):
    # Assuming the data is stored in a file named "water_balance_data.txt"
    

    # Read the data into a pandas DataFrame
    water_balance_data = pd.read_table(file_path, skiprows=5, delim_whitespace=True)
    water_balance_data = water_balance_data.drop(0)
    print(water_balance_data.columns)
    # Convert the columns to the appropriate data types
    water_balance_data["DATE"] = pd.to_datetime(
        water_balance_data[["DAY", "YR"]].astype(str).agg(' '.join, axis=1),
        format='%j %Y'
    )

    water_balance_data["ET"] = water_balance_data["ET"].astype(float)
    return water_balance_data

file_path = "c1_veg_out/water_veg.txt"
water_veg_data = createTable(file_path)
water_veg_data= water_veg_data[water_veg_data["DATE"].dt.year <= 1992]

file_path = "out/water_veg.txt"
water_veg_desert_data = createTable(file_path)
water_veg_desert_data = water_veg_desert_data[water_veg_desert_data["DATE"].dt.year <= 1992]


# Plot ET vs Date
plt.figure(figsize=(10, 6))
plt.plot(water_veg_data["DATE"], water_veg_data["PRECIP"], marker='o', linestyle='-', label = 'Silty with vegetation', linewidth=1)
plt.plot(water_veg_desert_data["DATE"], water_veg_desert_data["PRECIP"], marker='o', linestyle='-', label = 'Sandy with vegetation', linewidth=1)
plt.legend()
plt.xlabel("Date")
plt.ylabel("Precipitation in mm")
plt.title("Precipitation vs Date")
plt.grid(True)
plt.yticks([0, 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150])
plt.savefig('output_plot.png')


