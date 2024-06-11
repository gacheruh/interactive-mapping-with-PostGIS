import psycopg2
import geojson
from geojson import Feature, FeatureCollection, Point

# Database connection parameters
conn_params = {
    'dbname': 'innovation_hubss',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the database
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

# Fetch data from the database
cursor.execute("SELECT name, latitude, longitude, specialization, membership_profiles, focus_areas, city, website FROM hubs")
rows = cursor.fetchall()

# Create GeoJSON features
features = []
for row in rows:
    point = Point((row[2], row[1]))  # (longitude, latitude)
    features.append(
        Feature(
            geometry=point,
            properties={
                'Name': row[0],
                'Specialization': row[3],
                'Membership_Profiles': row[4],
                'Focus_Areas': row[5],
                'City': row[6], 
                'Website': row[7]
            }
        )
    )

# Create a FeatureCollection
feature_collection = FeatureCollection(features)

# Write to a GeoJSON file
with open('innovation_hubs.geojson', 'w') as f:
    geojson.dump(feature_collection, f)

# Close the connection
cursor.close()
conn.close()
