# Innovation Hubs Mapping Project
## Overview
This project maps and visualizes innovation hubs in Kenya using a relational database with geospatial capabilities (PostgreSQL with PostGIS) and an interactive web map (Leaflet). The map displays each hub's location, specialization, membership profiles, focus areas, and contact details.

## Features
* Data Storage: Uses PostgreSQL with PostGIS for geospatial data storage.
* Data Import: Imports data from a CSV file.
* Data Export: Converts data to GeoJSON format for web mapping.
* Web Map: Interactive map created with Leaflet.

## Prerequisites
* PostgreSQL with PostGIS extension
* Python 3.x with pandas, psycopg2, and geojson libraries
* A web server to host the HTML and GeoJSON files
## Setup Instructions
### 1. Install PostgreSQL and PostGIS
Install PostgreSQL and PostGIS on your system. For Ubuntu/Debian, use the apt package manager. For Windows or Mac, download the installer from the PostgreSQL website.

### 2. Set Up the Database
#### 1. Create the Database and Enable PostGIS:
* Create a new database and enable the PostGIS extension within that database.
#### 2. Create the hubs Table:
* Define a table to store the innovation hubs' data, including columns for name, latitude, longitude, specialization, membership profiles, focus areas, contact details, and a geography column for spatial data.

### 3. Import Data from CSV
#### 1. Prepare Your CSV File:
* Structure your CSV file with the required columns (name, latitude, longitude, specialization, membership profiles, focus areas, contact details).

#### 2. Copy Data into the Database:
* Use the COPY command in PostgreSQL to import the CSV data into the hubs table.
#### 3. Update the Geometry Column:
* Populate the geography column using the longitude and latitude data to enable spatial queries.

### 4. Export Data as GeoJSON
#### 1. Install Required Python Libraries:
* Install pandas, psycopg2, and geojson using pip.
#### 2. Run the Export Script:
* Write and execute a Python script to fetch data from the PostgreSQL database, create GeoJSON features, and save them to a GeoJSON file.
### 5. Create the Web Map
#### 1. Create an HTML File:
* Develop an HTML file to set up a Leaflet map. Include the necessary Leaflet CSS and JavaScript libraries.
#### 2. Load GeoJSON Data:
* Use the Fetch API to load the GeoJSON data and add it to the Leaflet map. Configure popups to display hub information.
### 6. Host the HTML and GeoJSON Files
#### 1. Upload Files to Your Web Server:

* Place the index.html and innovation_hubs.geojson files in your website’s directory.
#### 2. Ensure Correct Paths:

* Verify that the path to the GeoJSON file in your HTML file is correct.
#### 3. Access the Map:

* Open your website in a browser to see the interactive map with the innovation hubs plotted and popups showing their details.
## Summary
By following these steps, you can effectively map innovation hubs in Kenya, leveraging PostgreSQL with PostGIS for data storage and Leaflet for interactive web mapping. This setup ensures efficient data management and interactive visualization, providing valuable insights into the innovation ecosystem in Kenya.
