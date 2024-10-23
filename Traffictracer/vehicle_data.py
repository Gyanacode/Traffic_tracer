import pandas as pd
import random

# Create simulated vehicle data
num_samples = 100
data = []
for _ in range(num_samples):
    lat = random.uniform(34.0, 35.0)  # Simulated latitude
    lon = random.uniform(-118.0, -117.0)  # Simulated longitude
    speed = random.uniform(0, 100)  # Speed in km/h
    road_type = random.choice(['highway', 'service road'])  # Randomly choosing road type
    data.append((lat, lon, speed, road_type))

# Save to CSV
vehicle_data_df = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Speed', 'RoadType'])
vehicle_data_df.to_csv('vehicle_data.csv', index=False)